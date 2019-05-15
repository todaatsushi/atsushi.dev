from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (DetailView, ListView, UpdateView, DeleteView, CreateView)
from django.urls import reverse

from work.models import Project
from work.forms import CreateProject
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


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'work/detail.html'
    context_object_name = 'project'
    slug_field = 'url_slug'


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'work/update.html'
    fields = [
        'name', 'description', 'link', 'repository', 'languages', 'stack', 'hosting',
    ]
    slug_field = 'url_slug'

    def form_valid(self, form):
        form.instance.url_slug = form.instance.name.lower().replace(' ', '-')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view-project', kwargs={'slug': self.object.url_slug})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'work/delete.html'
    slug_field = 'url_slug'
    success_url = '/work/'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'work/create.html'
    form_class = CreateProject

    def form_valid(self, form):
        form.instance.url_slug = form.instance.name.lower().replace(' ', '-')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view-project', kwargs={'slug': self.object.url_slug})
