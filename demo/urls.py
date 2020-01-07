from django.urls import path
from . import views


app_name = 'demo'

urlpatterns = [
    path('records/', views.RecordListView.as_view(), name='records'),
    path('record/<int:pk>', views.RecordDetailView.as_view(), name='record-detail'),
    path('records-json/', views.RecordListJsonView.as_view(), name='records-json'),
]
