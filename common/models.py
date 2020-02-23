from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext


class User(AbstractBaseUser):
    # file_prepend = "users/profile_pics"
    username = models.CharField(_('user.username'), max_length=100, unique=True)
    password = models.CharField(_('user.password'), max_length=128)
    first_name = models.CharField(_('user.first_name'), max_length=150, blank=True)
    last_name = models.CharField(_('user.last_name'), max_length=150, blank=True)
    email = models.EmailField(_('user.email'), max_length=255, unique=True)
    last_login = models.DateTimeField(_('user.last_login'), blank=True, null=True)
    is_active = models.BooleanField(_('user.is_active'), default=True)
    is_superuser = models.BooleanField(_('user.is_superuser'), default=False)
    is_staff = models.BooleanField(_('user.is_staff'), default=False)
    date_joined = models.DateTimeField(_('user.date_joined'), auto_now_add=True)
    # role = models.CharField(_('user.role'), max_length=50, choices=ROLES)
    # profile_pic = models.FileField(_('user.profile_pic'), max_length=1000, upload_to=img_url, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
