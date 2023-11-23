"""
Serializers for the user API View.
"""

from django.contrib.auth import get_user_model
from core import models
from rest_framework import serializers
from djoser.serializers import (
    UserSerializer,
    UserCreateSerializer,
)


class CreateUserSerializer(UserCreateSerializer):
    """Serializer for the user object."""

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ("dob", "gender")


class CurrentUserSerializer(UserSerializer):
    """Serializer for the user object."""

    profession = serializers.CharField(source="get_profession_display")
    industry = serializers.StringRelatedField()
    institute = serializers.StringRelatedField()
    major = serializers.StringRelatedField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            "profession",
            "industry",
            "institute",
            "major",
        )


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = ["name"]


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = ["name"]


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Major
        fields = ["name"]
