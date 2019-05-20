from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.views.generic import (DetailView, ListView, UpdateView, DeleteView, CreateView)
from django.urls import reverse

from work.models import Project
from work.forms import CreateUpdateProject
from work.helper import unpack

LANGUAGES = unpack([
    l.languages for l in Project.objects.all()
])

TECHNOLOGIES = unpack ([
    t.stack for t in Project.objects.all()
])


class ProjectIndexView(ListView):
    model = Project
    template_name = 'work/index.html'
    context_object_name = 'all_projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['langs'] = LANGUAGES
        context['techs'] = TECHNOLOGIES
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

    def get_object(self, queryset=None):
        project = super().get_object(queryset=queryset)

        if self.request.user.is_authenticated:
            return project

        if not project.public:
            raise Http404()
        return project


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'work/update.html'
    form_class = CreateUpdateProject
    slug_field = 'url_slug'
    login_url = '/'
    redirect_field_name = 'redirect_to'

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
