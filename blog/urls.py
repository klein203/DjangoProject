from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.index, name='index'),
    # path(r'^(?P<blog_id>[0-9]+)', views.detail, name='detail'),
]