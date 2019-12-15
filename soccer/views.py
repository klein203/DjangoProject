from django.shortcuts import render
from django.views import generic
from .models import Match


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'soccer/index.html'
    context_object_name = 'latest_match_list'

    def get_queryset(self):
        # return Match.objects.filter(pub_date__lte=timezone.now())
        return Match.objects.order_by('schedule_date')
