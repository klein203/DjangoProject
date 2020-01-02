from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Match
import json


# Create your views here.
def matches(request):
    return render(request, template_name='soccer/match.html')


# @csrf_exempt
def api_match_fetch_all(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps("do not support GET method"), content_type="application/json")

    print('==========================api_match_fetch_all===========================')
    for item in request.POST.items():
        print(item)

    all_matches = Match.objects.order_by('schedule_date')

    draw = int(request.POST['draw'])
    print("draw =", draw)
    start = int(request.POST['start'])
    print("start =", start)
    length = int(request.POST['length'])
    print("length =", length)
    paginator = Paginator(object_list=all_matches, per_page=length)

    matches = None
    try:
        # print("page index (est.) =", start // length)
        matches = paginator.page(start // length)
    except PageNotAnInteger:
        matches = paginator.page(1)
    except EmptyPage:
        matches = paginator.page(paginator.num_pages)

    data = list()
    for m in matches.object_list:
        match = {
            "schedule": "%s" % m.schedule,
            "home_team": "%s" % m.home_team,
            "home_score": m.home_score,
            "away_score": m.away_score,
            "away_team": "%s" % m.away_team,
            "schedule_date": "%s" % m.schedule_date,
            "match_date": "%s" % m.match_date,
            "create_time": "%s" % m.create_time,
            "update_time": "%s" % m.update_time
        }
        data.append(match)

    resp = {
        'draw': draw,
        'recordsTotal': paginator.count,
        'recordsFiltered': paginator.count,
        'data': data
    }
    print('==========================api_match_fetch_all===========================')
    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def index(request):
    return render(request, 'index.html', locals())


def charts(request):
    return render(request, 'soccer/charts.html', locals())
