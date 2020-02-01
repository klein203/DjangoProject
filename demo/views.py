from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Record
from core.common.list import JsonListView
from django.http.response import JsonResponse
import datetime


# Create your views here.
class RecordListView(ListView):
    model = Record
    paginate_by = 5
    # template_name = 'demo/record_list.html'
    # context_object_name = 'object'

    # def get_queryset(self):
    #     return Record.objects.all()


class RecordListJsonView(JsonListView):
    model = Record
    paginate_by = 5


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    # template_name = 'demo/record_detail.html'


def test_json(request):
    kw = {'code': 0,
          'msg': 'success',
          'data': [
              {
                  'id': 1,
                  'name': 'a1'
              },
              {
                  'id': 2,
                  'name': 'b2'
              },
              {
                  'id': 3,
                  'name': 'c3'
              }
          ],
          'page': {
              'page_size': 5,
              'page': 1
          }}

    kw2 = {
        'id': 1,
        'name': 'aaa',
        'gender': 'M',
        'date_of_birth': datetime.date(1981, 1, 1),
        'create_time': datetime.datetime.now(),
        'update_time': datetime.datetime.now()
    }
    record = Record(kw2)

    return JsonResponse(record, safe=False)
