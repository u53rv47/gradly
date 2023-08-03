"""
Views for feed APIs.
"""

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from feed import serializers
from core.models import Post, Comment, Like


class PostListViewSet(viewsets.ModelViewSet):
    """ViewSet for feed APIs."""

    serializer_class = serializers.PostListSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    http_method_names = ["get"]


class PostDetailViewSet(viewsets.ModelViewSet):
    """ViewSet for feed APIs."""

    serializer_class = serializers.PostDetailSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    http_method_names = ["get"]
