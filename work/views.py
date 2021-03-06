from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import (DetailView, ListView, DeleteView, CreateView)
from django.urls import reverse

from work.models import Project, ProjectSpecs
from work.forms import CreateUpdateProject, CreateUpdateSpecs
from work.helper import unpack


class ProjectIndexView(ListView):
    model = Project
    template_name = 'work/index.html'
    context_object_name = 'all_projects'

    def get_context_data(self, **kwargs):
        """
        Generate all possible slicers (langs, techs and misc) to create class tags for filtering.
        """
        context = super().get_context_data(**kwargs)

        LANGUAGES = unpack([
            proj.languages for proj in Project.objects.filter(public=True)
        ])

        TECHNOLOGIES = unpack ([
            proj.stack for proj in Project.objects.filter(public=True)
        ])

        TAGS = unpack([
            proj.extra_tags for proj in Project.objects.filter(public=True)
        ])

        context['filters'] = {
            'Languages': LANGUAGES,
            'Technologies': TECHNOLOGIES,
            'Other / Skills': TAGS,
        }
        context['show_nav'] = True
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Project.objects.all()
        return Project.objects.filter(public=True).order_by('name')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'work/detail.html'
    context_object_name = 'project'
    slug_field = 'url_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_nav'] = True
        return context

    def get_object(self, queryset=None):
        """
        Show project unless the project is not public.
        """
        project = super().get_object(queryset=queryset)

        if self.request.user.is_authenticated:
            return project

        if not project.public:
            raise Http404()
        return project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'work/create.html'
    form_class = CreateUpdateProject
    redirect_field_name = None

    def form_valid(self, form):
        import re
        
        # Make valid URL_SLUG
        slug = form.instance.name.lower()
        slug = slug.replace(" ", "-")
        slug = re.sub(r'[^a-zA-Z0-9-]', '', slug)

        form.instance.url_slug = slug

        # Ensure there is only one current project
        if form.instance.current:
            for p in Project.objects.all():
                p.current = False
                p.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view-project', kwargs={'slug': self.object.url_slug})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'work/delete.html'
    slug_field = 'url_slug'
    success_url = '/work/'
    redirect_field_name = None



def project_update(request, slug):
    """
    Used in place of CBV in order to accomodate 2 different forms.
    """
    # Make sure project exists
    project = get_object_or_404(Project, url_slug=slug)

    # Form handling
    if request.method == 'POST':
        project_form = CreateUpdateProject(request.POST,
                                           instance=project
                                           )
        specs_form = CreateUpdateSpecs(
            request.POST,
            request.FILES,
            instance=project.projectspecs)

        if project_form.is_valid() and specs_form.is_valid():
            import re

            # Make valid URL_SLUG
            slug = project_form.instance.name.lower()
            slug = slug.replace(" ", "-")
            slug = re.sub(r'[^a-zA-Z0-9-]', '', slug)

            project_form.instance.url_slug = slug

            # Ensure there is only one current project
            if project_form.instance.current:
                for p in Project.objects.all():
                    p.current = False
                    p.save()

            project_form.save()
            specs_form.save()
            
            return HttpResponseRedirect(reverse('view-project', kwargs={
                'slug': slug
            }))

    # Populate form
    project_form = CreateUpdateProject(instance=project)
    specs_form = CreateUpdateSpecs(instance=project.projectspecs)
    
    context = {
        'project': project,
        'forms': [project_form, specs_form]
    }

    return render(request, 'work/update.html', context)
