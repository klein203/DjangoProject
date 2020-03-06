from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.views.generic import TemplateView
from .models import User
from .serializers import UserSerializer

# from django.utils.translation import gettext as _


class UserApiViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_serializer_class(self):
        pass
        # https://blog.51cto.com/haoyonghui/2425999


class UserListView(TemplateView):
    template_name = 'common/user_list.html'


class UserDetailView(TemplateView):
    template_name = 'common/user_detail.html'


class UserCreateView(TemplateView):
    template_name = 'common/user_form.html'
