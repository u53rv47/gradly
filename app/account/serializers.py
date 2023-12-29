"""
Serializers for the user API View.
"""

from django.contrib.auth import get_user_model
from core.models import (
    Institute,
    Industry,
    Major,
)
from rest_framework import serializers
from djoser.serializers import UserSerializer


class CurrentUserSerializer(UserSerializer):
    """Serializer for the user object."""

    # dob = serializers.DateField()
    # gender = serializers.CharField(source="get_gender_display")
    profession = serializers.CharField(source="get_profession_display")
    industry = serializers.CharField()
    institute = serializers.CharField()
    major = serializers.CharField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            "dob",
            "gender",
            "profession",
            "industry",
            "institute",
            "major",
        )

    def update(self, instance, validated_data):
        print(validated_data)
        industry_name = validated_data.pop("industry", None)
        if industry_name is not None:
            industry, created = Industry.objects.get_or_create(name=industry_name)
            instance.industry = industry

        institute_name = validated_data.pop("institute", None)
        if institute_name is not None:
            institute, created = Institute.objects.get_or_create(name=institute_name)
            instance.institute = institute

        major_name = validated_data.pop("major", None)
        if major_name is not None:
            major, created = Major.objects.get_or_create(name=major_name)
            instance.major = major

        return super().update(instance, validated_data)


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = ["name"]


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ["name"]


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ["name"]
