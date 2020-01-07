from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Record
from DjangoProject.common.list import JsonListView


# Create your views here.
class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    paginate_by = 5
    # template_name = 'demo/record_list.html'
    # context_object_name = 'object'

    # def get_queryset(self):
    #     return Record.objects.all()


class RecordListJsonView(LoginRequiredMixin, JsonListView):
    model = Record
    paginate_by = 5
    template_name = 'demo/record_json_list.html'


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    # template_name = 'demo/record_detail.html'
