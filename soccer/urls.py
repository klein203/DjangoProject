from django.urls import path

from . import views

app_name = 'soccer'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.dashboard, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('matches', views.matches, name='matches'),
    path('charts', views.charts, name='charts'),
]