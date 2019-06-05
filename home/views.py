import os
from random import randint

from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse
from django.db.models import Model

from home.forms import ContactForm
from home.models import Feedback, SongPick

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
        context['hide_nav'] = False
        return context


def home(request):
    try:
        current = Project.objects.get(current=True)
    except Model.DoesNotExist:
        current = None

    context = {
        'projects': Project.objects.all(),
        'hide_nav': True,
        'current': current,
    }
    return render(request, 'home/home.html', context)


def about(request):
    try:
        current = Project.objects.get(current=True)
    except Model.DoesNotExist:
        current = None

    song = SongPick.objects.get(
        id=randint(1, SongPick.objects.last().id)
    )

    context = {
        'projects': Project.objects.all(),
        'hide_nav': False,
        'current': current,
        'song': song,
    }
    return render(request, 'home/about.html', context)


def test(request):
    return render(request, 'home/500.html')
