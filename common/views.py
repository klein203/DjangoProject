from django.shortcuts import render
from django.views.generic import ListView
from .models import User
from django.utils.translation import gettext as _


# Create your views here.
class UserListView(ListView):
    model = User
    # paginate_by = 1
