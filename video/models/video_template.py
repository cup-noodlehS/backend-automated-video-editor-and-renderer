from django.db import models

from video.models.file import File, Font, AeVersion
from organization.models import Organization
from django.contrib.auth import get_user_model


class VideoTemplate(models.Model):
    '''
    **Fields:**
    - name: CharField
    - file: ForeignKey to `File` model, required.
    - ae_version: ForeignKey to `AeVersion` model, optional (can be null), and uses `SET_NULL` on deletion.
    - fonts: ManyToManyField to `Font` model, optional.
    - composition_name: CharField, represents the name of the composition in the video template.
    - status: IntegerField with choices to indicate if the video template is in testing or finalized. Defaults to `TESTING`.
    - created_at: DateTimeField that automatically stores the timestamp when the instance is created.
    - updated_at: DateTimeField that automatically updates the timestamp when the instance is modified.
    - creator: ForeignKey to the user model (custom user), indicates who created the video template.
    - organization: ForeignKey to `Organization` model, indicates which organization the template belongs to.
    '''

    TESTING = 0
    FINALIZED = 1
    STATUS_CHOICES = [
        (TESTING, 'Testing'),
        (FINALIZED, 'Finalized')
    ]

    name = models.CharField(max_length=255)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    ae_version = models.ForeignKey(AeVersion, null=True, on_delete=models.SET_NULL, blank=True, related_name='video_templates')
    fonts = models.ManyToManyField(Font, related_name='video_templates', blank=True, null=True)
    composition_name = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICES, default=TESTING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='video_templates')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='video_templates')

    @property
    def status_display(self):
        return dict(self.STATUS_CHOICES)[self.status]

    def __str__(self):
        return self.name


class StaticLayer(models.Model):
    '''
    **Fields:**
    - layer_name: CharField
    - video_template: ForeignKey to `VideoTemplate` model, required.
    - layer_type: IntegerField to indicate the type of the layer (image, video, or audio).
    - file: ForeignKey to `File` model, required.
    '''

    IMAGE = 0
    VIDEO = 1
    AUDIO = 2
    LAYER_TYPE_CHOICES = [
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
        (AUDIO, 'Audio')
    ]

    layer_name = models.CharField(max_length=255)
    video_template = models.ForeignKey(VideoTemplate, on_delete=models.CASCADE, related_name='static_layers')
    layer_type = models.IntegerField(choices=LAYER_TYPE_CHOICES)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    @property
    def layer_type_display(self):
        return dict(self.LAYER_TYPE_CHOICES)[self.layer_type]

    def __str__(self):
        return self.layer_name


class DynamicLayer(models.Model):
    '''
    **Fields:**
    - layer_name: CharField to store the name of the dynamic layer.
    - display_name: CharField to store the display name of the layer.
    - video_template: ForeignKey to `VideoTemplate`, representing the template to which the dynamic layer belongs.
    - layer_type: IntegerField to indicate the type of the layer (data, image, video, or audio).
    - helper_text: TextField to store optional instructions or hints for the layer.
    - value: CharField to store a dynamic value for the layer, optional.
    - file: ForeignKey to `File`, optional, representing the associated media file for the layer.
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

    layer_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    video_template = models.ForeignKey(VideoTemplate, on_delete=models.CASCADE, related_name='dynamic_layers')
    layer_type = models.IntegerField(choices=LAYER_TYPE_CHOICES)
    helper_text = models.TextField(blank=True, null=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def layer_type_display(self):
        return dict(self.LAYER_TYPE_CHOICES)[self.layer_type]
    
    def __str__(self):
        return self.layer_name