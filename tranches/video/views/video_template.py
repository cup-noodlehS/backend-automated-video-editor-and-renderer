from tranches.utils.generic_api import GenericView

from video.models import VideoTemplate, StaticLayer, DynamicLayer
from video.serializers import VideoTemplateSerializer, StaticLayerSerializer, DynamicLayerSerializer


class VideoTemplateView(GenericView):
    queryset = VideoTemplate.objects.all()
    serializer_class = VideoTemplateSerializer


class StaticLayerView(GenericView):
    queryset = StaticLayer.objects.all()
    serializer_class = StaticLayerSerializer


class DynamicLayerView(GenericView):
    queryset = DynamicLayer.objects.all()
    serializer_class = DynamicLayerSerializer
