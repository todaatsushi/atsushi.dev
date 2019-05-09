from django.urls import path

from work import views as v

urlpatterns = [
    path('', v.ProjectIndexView.as_view(), name='all-projects'),
    path('create/', v.ProjectCreateView.as_view(), name='new-project'),
    path('<str:name>/', v.ProjectDetailView.as_view(), name='view-project'),
    path('<str:name>/update/', v.ProjectUpdateView.as_view(), name='update-project'),
    path('<str:name>/delete/', v.ProjectDeleteView.as_view(), name='delete-project'),
]
