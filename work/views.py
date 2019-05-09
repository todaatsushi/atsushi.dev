from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, FormView

from work.models import Project


class ProjectIndexView(ListView):
    model = Project
    template_name = 'work/index.html'
    context_object_name = 'all_projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'work/prject_layout.html'
    context_object_name = 'project'


class ProjectUpdateView(UpdateView):
    pass


class ProjectDeleteView(DeleteView):
    pass


class ProjectCreateView(FormView):
    pass
