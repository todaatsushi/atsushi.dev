import os

from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse

from home.forms import ContactForm
from home.models import Feedback

from work.models import Project


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = '/contact/'
    success_message = 'Thanks for contacting me. You can expect a reply back very soon.'

    def form_valid(self, form):
        if form.is_valid():
            feedback = Feedback(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                message=form.cleaned_data.get('message'),
                score=form.cleaned_data.get('score'),
            )

            feedback.save()
            my_email = os.environ.get('EMAIL_ADDRESS')
            send_mail(
                f'Contact Email from {feedback.name} ({feedback.email})',
                feedback.message,
                my_email,
                [my_email],
                fail_silently=False
            )

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


def home(request):
    context = {
        'projects': Project.objects.all(),
        'show_nav': False,
        'current': Project.objects.get(current=True)
    }
    return render(request, 'home/home.html', context)


def about(request):
    context = {
        'projects': Project.objects.all(),
        'show_nav': True,
    }
    return render(request, 'home/about.html', context)
