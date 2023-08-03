"""
Serializars for home app.
"""

from rest_framework import serializers

from core.models import User, Post, Comment

from home.serializers import CommunitySerializer


class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "image"]
        read_only_fields = ["id"]


class PostListSerializer(serializers.ModelSerializer):
    """Serializer for "retrieval" of post list for Feed/Home."""

    user = FeedUserSerializer(read_only=True)
    community = CommunitySerializer(read_only=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    comment_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "community",
            "title",
            "content",
            "image",
            "created_at",
            "likes",
            "comment_count",
        ]
        read_only_fields = fields


class CommentDetailSerializer(serializers.ModelSerializer):
    """Comment Serializer for GET with post."""

    # Refer https://stackoverflow.com/questions/13376894/django-rest-framework-nested-self-referential-objects for parent-child relationship

    user = FeedUserSerializer(read_only=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "content", "created_at", "likes", "children"]

    # def get_related_field(self, model_field):
    #     # Handles initializing the `children` field
    #     return CommentDetailSerializer()


class PostDetailSerializer(PostListSerializer):
    """Serializer for Detailed page view of a post with comments & replies"""

    comments = CommentDetailSerializer(many=True, required=False)

    class Meta(PostListSerializer.Meta):
        model = Post
        fields = PostListSerializer.Meta.fields + ["comments", "tags"]
