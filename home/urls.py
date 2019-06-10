from django.urls import path

from home import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('contact/', v.ContactView.as_view(), name='contact'),
    path('about/', v.about, name='about'),
    path('test/', v.test, name='test'),
]
