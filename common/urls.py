from django.urls import path, include
from . import views


app_name = 'common'

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='users'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
]
