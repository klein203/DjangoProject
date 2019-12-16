from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.index, name='index'),
    path('<int:blog_id>/detail', views.detail, name='detail'),
]