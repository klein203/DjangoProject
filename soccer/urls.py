from django.urls import path
from . import views


app_name = 'soccer'

urlpatterns = [
    path('', views.index, name='index'),
    path('match', views.matches, name='match'),
    path('api/match/fetch_all', views.api_match_fetch_all, name='api_match_fetch_all'),
    path('charts', views.charts, name='charts'),
]
