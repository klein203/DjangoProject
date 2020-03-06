from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

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
