from django.contrib.auth import views
from django.urls import reverse_lazy
from django.shortcuts import render


# Create your views here.
class AccountsLoginView(views.LoginView):
    pass


class AccountsLogoutView(views.LogoutView):
    pass


class AccountsPasswordResetView(views.PasswordResetView):
    template_name = 'registration/pwd_reset_form.html'
    email_template_name = 'registration/pwd_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class AccountsPasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'registration/pwd_reset_done.html'


class AccountsPasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = 'registration/pwd_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class AccountsPasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'registration/pwd_reset_complete.html'


class AccountsPasswordChangeView(views.PasswordChangeView):
    template_name = 'registration/pwd_change_form.html'
    success_url = reverse_lazy('accounts:pwd_change_done')


class AccountsPasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'registration/pwd_change_done.html'
