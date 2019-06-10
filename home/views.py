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
from work.helper import get_current_or_dummy


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = '/contact/'
    success_message = 'Thanks for contacting me. You can expect a reply back very soon.'

    def form_valid(self, form):
        """
        Use valid form data to send an email to the admin.
        """
        if form.is_valid():
            feedback = Feedback(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                message=form.cleaned_data.get('message'),
                score=form.cleaned_data.get('score'),
            )

            feedback.save()
            admin_email = os.environ.get('EMAIL_ADDRESS')
            send_mail(
                f'Contact Email from {feedback.name} ({feedback.email})',
                feedback.message,
                admin_email,
                [admin_email],
                fail_silently=False
            )

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Home nav is sticky and not formatted like the rest of the site.
        context['hide_nav'] = False
        return context


def home(request):
    context = {
        'projects': Project.objects.all(),
        'hide_nav': True,
        'current': get_current_or_dummy(),
    }
    return render(request, 'home/home.html', context)


def about(request):
    # Song recommendation
    song = SongPick.objects.get(
        id=randint(1, SongPick.objects.last().id)
    )

    context = {
        'projects': Project.objects.all(),
        'hide_nav': False,
        'current': get_current_or_dummy(),
        'song': song,
        'form': ContactForm,
    }
    return render(request, 'home/about.html', context)


# def test(request):
#     """
#     Test view to see if templates work.
#     """
#     return render(request, 'home/500.html')
