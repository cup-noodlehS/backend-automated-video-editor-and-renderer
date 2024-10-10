from rest_framework import serializers

from .models import Organization, OrganizationMember, Credits
from accounts.serializers import UserSerializer



class OrganizationSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    creator = UserSerializer(read_only=True)
    creator_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Organization
        fields = "__all__"


class OrganizationMemberSerializer(serializers.ModelSerializer):
    organization_id = serializers.IntegerField(write_only=True)
    organization = OrganizationSerializer(read_only=True)
    member = UserSerializer(read_only=True)
    added_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = OrganizationMember
        fields = "__all__"


class CreditsSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.IntegerField(write_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    start = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Credits
        fields = "__all__"