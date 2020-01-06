from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Record


# Create your views here.
class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    # template_name = 'demo/record_list.html'
    # context_object_name = 'object'

    # def get_queryset(self):
    #     return Record.objects.all()


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    # template_name = 'demo/record_detail.html'
