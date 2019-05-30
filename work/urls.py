from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import work.views as v

urlpatterns = [
    path('', v.ProjectIndexView.as_view(), name='all-projects'),
    path('create/', v.ProjectCreateView.as_view(), name='new-project'),
    path('<slug:slug>/', v.ProjectDetailView.as_view(), name='view-project'),
    path('<slug:slug>/update/', v.project_update, name='update-project'),
    path('<slug:slug>/delete/', v.ProjectDeleteView.as_view(), name='delete-project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
