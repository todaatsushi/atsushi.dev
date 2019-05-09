from django.shortcuts import render
from django.views.generic import (DetailView, ListView, UpdateView, DeleteView, CreateView)

from work.forms import CreateUpdateProject
from work.models import Project


class ProjectIndexView(ListView):
    model = Project
    template_name = 'work/index.html'
    context_object_name = 'all_projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'work/detail.html'
    context_object_name = 'project'


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'work/update.html'
    form_class = CreateUpdateProject
    success_url = '/work/'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = '/work/'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'work/create.html'
    form_class = CreateUpdateProject
    success_url = '/work/'
