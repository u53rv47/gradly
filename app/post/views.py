"""
Views for post APIs.
"""

from rest_framework import (
    viewsets,
    mixins,
    status,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from post import serializers

from core.models import Tag, Post, Comment, Like


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for post APIs."""

    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()
    # queryset = Post.objects.prefetch_related("comments").all()

    def perform_create(self, serializer):
        """Create a new post."""
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """Create a new post."""
        serializer.save(user=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """Create a new post."""
        serializer.save(user=self.request.user)
