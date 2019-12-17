from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Match

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'soccer/index.html'
#     context_object_name = 'latest_match_list'
#
#     def get_queryset(self):
#         # return Match.objects.filter(pub_date__lte=timezone.now())
#         return Match.objects.order_by('schedule_date')

# def detail(request, question_id):
#     question = get_object_or_404(Match, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

def matches(request):
    all_matches = Match.objects.order_by('schedule_date')
    paginator = Paginator(all_matches, 10, 2)
    page = request.GET.get('page')
    try:
        matches = paginator.page(page)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)

    context = {
        'matches': matches,
    }
    return render(request, template_name='soccer/tables.html', context=context)

def dashboard(request):
    return render(request, 'soccer/dashboard.html', locals())

def charts(request):
    return render(request, 'soccer/charts.html', locals())
