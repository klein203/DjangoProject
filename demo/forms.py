from django.forms import ModelForm
from .models import Simple


class SimpleModelForm(ModelForm):
    class Meta:
        model = Simple
        fields = "__all__"
