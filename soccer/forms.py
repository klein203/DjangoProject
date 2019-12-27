from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Test


class RegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name',]


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'age',]
