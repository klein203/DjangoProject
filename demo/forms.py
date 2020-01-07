from django.forms import ModelForm
from .models import Record


class RecordModelForm(ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
