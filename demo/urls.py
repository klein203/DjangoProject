from django.urls import path
from . import views


app_name = 'demo'

urlpatterns = [
    path('', views.RecordListView.as_view(), name='records-default'),
    path('records/', views.RecordListView.as_view(), name='records'),
    path('record/<int:pk>', views.RecordDetailView.as_view(), name='record-detail'),
    path('records-json/', views.RecordListJsonView.as_view(), name='records-json'),
    # path('records-json/', views.test_json, name='records-json'),
]
