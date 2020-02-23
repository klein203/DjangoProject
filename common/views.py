from rest_framework import viewsets
from django.views.generic import TemplateView
from .models import User
from .serializers import UserSerializer


# from django.utils.translation import gettext as _


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserListView(TemplateView):
    template_name = 'common/user_list.html'


class UserDetailView(TemplateView):
    template_name = 'common/user_detail.html'


class UserCreateView(TemplateView):
    template_name = 'common/user_form.html'
