from django.db import transaction
from rest_framework import status
from rest_framework.response import Response

from tranches.utils.generic_api import GenericView
from tranches.utils.nexrender_server import get_all_render_jobs, get_render_job, render_video

from video.models import VideoVariant, VideoVariantLayer
from video.serializers import VideoVariantSerializer, VideoVariantLayerSerializer


class VideoVariantView(GenericView):
    queryset = VideoVariant.objects.all()
    serializer_class = VideoVariantSerializer
    
    @transaction.atomic
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            instance = serializer.save()
            self.cache_object(serializer.data, instance.pk)
            self.invalidate_list_cache()

            assets = self._prepare_assets(instance)
            
            job_id = render_video(
                template_uri=instance.video_template.file.url,
                composition_name=instance.video_template.composition_name,
                assets=assets,
                priority=0 if instance.is_test else 1
            )
            instance.job_id = job_id
            instance.save()
            
            updated_serializer = self.serializer_class(instance)
            return Response(updated_serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _prepare_assets(self, instance):
        assets = []
        for layer in instance.video_template.static_layers.all():
            assets.append({
                'type': layer.layer_type_display.lower(),
                'layerName': layer.layer_name,
                'src': layer.file.url
            })
        for layer in instance.layers.all():
            item = {
                'type': layer.layer_type_display.lower(),
                'layerName': layer.layer_name,
            }
            if layer.layer_type == VideoVariantLayer.DATA:
                item['property'] = 'Source Text'
                item['value'] = layer.value
            else:
                item['src'] = layer.file.url
            assets.append(item)
        return assets