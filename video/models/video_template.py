from django.db import models

from video.models.file import File, Font, AeVersion
from django.contrib.auth import get_user_model


class VideoTemplate(models.Model):
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

    def __str__(self):
        return self.name