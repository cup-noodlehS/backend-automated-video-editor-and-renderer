from rest_framework import serializers

from video.models import VideoTemplate, StaticLayer, DynamicLayer   
from video.serializers.file import FileSerializer, FontSerializer, AeVersionSerializer
from accounts.serializers import UserSerializer
from organization.serializers import OrganizationSerializer


class SimpleOrganizationSerializer(OrganizationSerializer):
    class Meta(OrganizationSerializer.Meta):
        fields = ('id', 'name')


class SimpleUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'full_name', 'first_name', 'last_name')


class SimpleFontsSerializer(FontSerializer):
    class Meta(FontSerializer.Meta):
        fields = ('id', 'name')


class VideoTemplateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True)
    ae_version = AeVersionSerializer(read_only=True)
    ae_version_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    fonts = SimpleFontsSerializer(many=True, read_only=True)
    fonts_id = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    composition_name = serializers.CharField(max_length=255)
    status = serializers.IntegerField()
    status_display = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    creator = SimpleUserSerializer(read_only=True)
    creator_id = serializers.IntegerField(write_only=True)
    organization = SimpleOrganizationSerializer(read_only=True)
    organization_id = serializers.IntegerField(write_only=True)
    sample_video = FileSerializer(read_only=True)
    sample_video_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = VideoTemplate
        fields = "__all__"


class SimpleVideoTemplateSerializer(VideoTemplateSerializer):
    class Meta(VideoTemplateSerializer.Meta):
        fields = ('id', 'name')



class StaticLayerSerializer(serializers.ModelSerializer):
    layer_name = serializers.CharField(max_length=255)
    video_template = SimpleVideoTemplateSerializer(read_only=True)
    video_template_id = serializers.IntegerField(write_only=True)
    layer_type = serializers.IntegerField()
    layer_type_display = serializers.CharField(read_only=True)
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = StaticLayer
        fields = "__all__"


class DynamicLayerSerializer(serializers.ModelSerializer):
    layer_name = serializers.CharField(max_length=255)
    display_name = serializers.CharField(max_length=255)
    video_template = SimpleVideoTemplateSerializer(read_only=True)
    video_template_id = serializers.IntegerField(write_only=True)
    layer_type = serializers.IntegerField()
    layer_type_display = serializers.CharField(read_only=True)
    helper_text = serializers.CharField(max_length=500, required=False, allow_blank=True)
    value = serializers.CharField(max_length=500, required=False, allow_blank=True)
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = DynamicLayer
        fields = "__all__"