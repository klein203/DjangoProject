from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', views.AccountsLoginView.as_view(), name='login'),
    path('logout/', views.AccountsLogoutView.as_view(), name='logout'),

    path('password_change/', views.AccountsPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.AccountsPasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', views.AccountsPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.AccountsPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.AccountsPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.AccountsPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
