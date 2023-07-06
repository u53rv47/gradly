"""
Views for home APIs.
"""

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from home import serializers

from core.models import Domain, Community, Tag, Post, Comment, Like


class DomainViewSet(viewsets.ModelViewSet):
    """ViewSet for domain APIs."""

    serializer_class = serializers.DomainDetailSerializer
    queryset = Domain.objects.all()
    http_method_names = ["get", "list"]

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == "list":
            return serializers.DomainSerializer

        return self.serializer_class


class CommunityViewSet(viewsets.ModelViewSet):
    """ViewSet for community APIs."""

    serializer_class = serializers.CommunityDetailSerializer
    queryset = Community.objects.all()
    http_method_names = ["get", "list"]

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == "list":
            return serializers.CommunitySerializer

        return self.serializer_class
