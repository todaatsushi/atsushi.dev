from django.urls import path

from work import views as v

urlpatterns = [
    path('', v.ProjectIndexView, name='all-projects'),
    path('create/', v.ProjectCreateView, name='new-project'),
    path('<str:name>/', v.ProjectDetailView, name='view-project'),
    path('<str:name>/update/', v.ProjectUpdateView, name='update-project'),
    path('<str:name>/delete/', v.ProjectDeleteView, name='delete-project'),
]
