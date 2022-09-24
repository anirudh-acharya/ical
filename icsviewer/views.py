from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Event


class IndexView(generic.ListView):
    template_name = 'icsviewer/index.html'
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        """Returns the first five events"""
        return Event.objects.order_by('start_date')[:5]


class DetailView(generic.DetailView):
    model = Event
    template_name = 'icsviewer/detail.html'

