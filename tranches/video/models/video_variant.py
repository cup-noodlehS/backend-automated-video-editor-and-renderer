from django.db import models
from django.contrib.auth import get_user_model

from video.models import File, VideoTemplate


class VideoVariant(models.Model):
    '''
    **Fields:**
    - video_template: ForeignKey to `VideoTemplate`, representing the video template that the variant is derived from.
    - name: CharField to store the name of the video variant.
    - video: ForeignKey to `File`, optional, representing the video file associated with this variant.
    - creator: ForeignKey to `User` (via `get_user_model()`), representing the creator of the video variant.
    - state: IntegerField to track the current status of the video variant (queued, rendering, uploading, etc.).
    - job_id: CharField to store the unique ID of the rendering/upload job.
    - finished_job_details: JSONField, optional, to store details about the completed job.
    - video_minutes: IntegerField to store the length of the video in minutes.
    - created_at: DateField to store the creation date (automatically populated).
    - updated_at: DateField to store the last modification date (automatically updated).
    
    **Status Choices:**
    - `STATUS_CHOICE`: A list of available status options for the `state` field.
        - QUEUED (0): Video is queued for rendering.
        - RENDERING (1): Video is currently being rendered.
        - UPLOADING (2): Video is being uploaded to the cloud.
        - SUCCESS (3): Video has been successfully processed.
        - FAILED (4): Processing of the video failed.
    '''

    QUEUED = 0
    RENDERING = 1
    UPLOADING = 2
    SUCCESS = 3
    FAILED = 4
    STATUS_CHOICE = [
        (QUEUED, 'Queued'),
        (RENDERING, 'Rendering'),
        (UPLOADING, 'Uploading'),
        (SUCCESS, 'Success'),
        (FAILED, 'Failed')
    ]

    video_template = models.ForeignKey(VideoTemplate, on_delete=models.CASCADE, related_name='video_variants')
    name = models.CharField(max_length=255)
    video = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='video_variants')
    state = models.IntegerField(choices=STATUS_CHOICE, default=QUEUED)
    job_id = models.CharField(max_length=255)
    finished_job_details = models.JSONField(null=True, blank=True)
    video_minutes = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_test = models.BooleanField(default=False)

    @property
    def state_display(self):
        return dict(self.STATUS_CHOICE)[self.state]
    
    def __str__(self):
        return self.name


class VideoVariantLayer(models.Model):
    '''
    **Fields:**
    - video_variant: ForeignKey to `VideoVariant`, representing the video variant to which this layer belongs.
    - layer_name: CharField to store the name of the layer (e.g., "Title", "Background Image").
    - layer_type: IntegerField to indicate the type of the layer (data, image, video, or audio).
    - file: ForeignKey to `File`, optional, representing the media file associated with this layer.
    - value: CharField to store a dynamic value for the layer (e.g., text data), optional.
    '''

    DATA = 0
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    LAYER_TYPE_CHOICES = [
        (DATA, 'Data'),
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
        (AUDIO, 'Audio')
    ]

    video_variant = models.ForeignKey(VideoVariant, on_delete=models.CASCADE, related_name='layers')
    layer_name = models.CharField(max_length=255)
    layer_type = models.IntegerField(choices=LAYER_TYPE_CHOICES)
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    value = models.CharField(max_length=500, null=True, blank=True)

    @property
    def layer_type_display(self):
        return dict(self.LAYER_TYPE_CHOICES)[self.layer_type]
    
    def __str__(self):
        return self.layer_name
