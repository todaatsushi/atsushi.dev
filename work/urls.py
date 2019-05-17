from django.urls import path

import work. views as v

urlpatterns = [
    path('', v.ProjectIndexView.as_view(), name='all-projects'),
    path('create/', v.ProjectCreateView.as_view(), name='new-project'),
    path('<slug:slug>/', v.ProjectDetailView.as_view(), name='view-project'),
    path('<slug:slug>/update/', v.ProjectUpdateView.as_view(), name='update-project'),
    path('<slug:slug>/delete/', v.ProjectDeleteView.as_view(), name='delete-project'),
]
