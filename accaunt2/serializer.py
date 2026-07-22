from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",

            "role",
        ]


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "avatar",
            "role",
            "password",
        ]

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"]
        )
        return UserModel.objects.create(**validated_data)