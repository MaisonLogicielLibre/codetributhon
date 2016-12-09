# coding: utf-8

from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from projects.models import Contribution
from django.db import connection


class Home(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        nb_contrib = Contribution.objects.filter( enabled=1).count()
        app = settings.CONSTANT
        context['objectif_of_contribution_binairy'] = "{0:b}".format(app['contribution'])
        context['objectif_of_contribution_decimal'] = app['contribution']
        context['nb_of_accepted_contribution'] = nb_contrib
        return context




class Contact(generic.TemplateView):
    template_name = 'pages/contact.html'


class Calendar(generic.TemplateView):
    template_name = 'pages/calendar.html'


class Settlement(generic.TemplateView):
    template_name = 'pages/settlement.html'

class Reward(generic.TemplateView):
    template_name = 'pages/reward.html'

class LogoutView(generic.RedirectView):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            'Vous avez été déconnecté!'
        )

        return redirect(self.get_redirect_url(*args, **kwargs))

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy(
            "pages:home"
        )
