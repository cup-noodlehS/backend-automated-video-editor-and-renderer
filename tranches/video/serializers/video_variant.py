from rest_framework import serializers

from video.models import VideoVariant, VideoVariantLayer
from video.serializers.video_template import SimpleVideoTemplateSerializer, SimpleUserSerializer
from video.serializers.file import FileSerializer


class VideoVariantSerializer(serializers.ModelSerializer):
    video_template = SimpleVideoTemplateSerializer(read_only=True)
    video_template_id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(max_length=255)
    video = FileSerializer(read_only=True)
    video_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    creator = SimpleUserSerializer(read_only=True)
    creator_id = serializers.IntegerField(write_only=True)
    state = serializers.IntegerField()
    state_display = serializers.CharField(read_only=True)
    job_id = serializers.CharField(max_length=255)
    finished_job_details = serializers.JSONField(required=False, allow_null=True)
    video_minutes = serializers.IntegerField()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    is_test = serializers.BooleanField()

    class Meta:
        model = VideoVariant
        fields = "__all__"


class SimpleVideoVariantSerializer(VideoVariantSerializer):
    class Meta(VideoVariantSerializer.Meta):
        fields = ('id', 'name')

class VideoVariantLayerSerializer(serializers.ModelSerializer):
    video_variant = SimpleVideoVariantSerializer(read_only=True)
    video_variant_id = serializers.IntegerField(write_only=True)
    layer_name = serializers.CharField(max_length=255)
    layer_type = serializers.IntegerField()
    layer_type_display = serializers.CharField(read_only=True)
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    value = serializers.CharField(max_length=500, required=False, allow_null=True)

    class Meta:
        model = VideoVariantLayer
        fields = "__all__"
