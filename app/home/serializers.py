"""
Serializars for home app.
"""

from rest_framework import serializers

from core.models import Domain, Community


class CommunitySerializer(serializers.ModelSerializer):
    """Serializer for community."""

    class Meta:
        model = Community
        fields = ["id", "name"]
        read_only_fields = ["id"]


class CommunityDetailSerializer(CommunitySerializer):
    """Serializer for community detail view."""

    class Meta(CommunitySerializer.Meta):
        fields = CommunitySerializer.Meta.fields + ["description"]


class DomainSerializer(serializers.ModelSerializer):
    """Serializer for domain."""

    communities = CommunitySerializer(many=True, required=True)

    class Meta:
        model = Domain
        fields = ["id", "name", "communities"]
        read_only_fields = ["id"]


class DomainDetailSerializer(DomainSerializer):
    """Serializer for domain detail view."""

    communities = CommunityDetailSerializer(many=True, required=True)

    class Meta(DomainSerializer.Meta):
        fields = DomainSerializer.Meta.fields + ["description"]
