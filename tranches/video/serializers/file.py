from rest_framework import serializers
from video.models import File, Font, AeVersion


class FileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = File
        fields = "__all__"


class FontSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    file = FileSerializer()

    class Meta:
        model = Font
        fields = "__all__"


class AeVersionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AeVersion
        fields = "__all__"
