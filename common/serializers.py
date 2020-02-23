from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email')
        fields = '__all__'
        extra_kwargs = {
            "password": {
                "write_only": True
            },
            "date_joined": {
                "read_only": True
            },
            "last_login": {
                "read_only": True
            },
        }
