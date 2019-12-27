from django.urls import path
from . import views
from .views import TestView


app_name = 'soccer'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.dashboard, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('match', views.matches, name='match'),
    path('api/match/fetch_all', views.api_match_fetch_all, name='api_match_fetch_all'),
    path('charts', views.charts, name='charts'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('test', TestView.as_view(), name='test'),
]