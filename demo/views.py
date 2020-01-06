from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Simple


# Create your views here.
class SimpleListView(LoginRequiredMixin, generic.ListView):
    model = Simple
    template_name = 'demo/simple_list.html'

    def get_queryset(self):
        return Simple.objects.all()
