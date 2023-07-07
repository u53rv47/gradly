"""
Serializars for post app.
"""

from rest_framework import serializers

from core.models import (
    Tag,
    Post,
    Comment,
    Like,
)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ["id", "name"]
        read_only_fields = ["id"]


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post create / update / delete APIs."""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ["id", "community", "title", "content", "image", "created_at", "tags"]
        read_only_fields = ["id"]

    def _get_or_create_tags(self, tags, post):
        """Handle getting or creating tags as needed."""
        auth_user = self.context["request"].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            post.tags.add(tag_obj)

    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop("tags", [])
        post = Post.objects.create(**validated_data)
        self._get_or_create_tags(tags, post)

        return post


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer for create / delete / update."""

    class Meta:
        model = Comment
        fields = ["id", "post", "content", "created_at", "replied_to"]
        read_only_fields = ["id"]

    # def get_related_field(self, model_field):
    #     # Handles initializing the `replied_to` field
    #     return CommentSerializer()


class LikeSerializer(serializers.ModelSerializer):
    """Serializer for like"""

    class Meta:
        model = Like
        fields = ["id", "post", "comment", "created_at", "reaction"]
        read_only_fields = ["id"]
