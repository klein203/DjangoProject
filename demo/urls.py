from django.urls import path
from . import views


app_name = 'demo'

urlpatterns = [
    path('simple/', views.SimpleListView.as_view(), name='simple'),
]
