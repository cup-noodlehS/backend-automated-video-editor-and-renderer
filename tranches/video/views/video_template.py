from tranches.utils.generic_api import GenericView

from video.models import VideoTemplate, StaticLayer, DynamicLayer
from video.serializers import DetailedVideoTemplateSerializer, VideoTemplateSerializer, StaticLayerSerializer, DynamicLayerSerializer


class DetailedVideoTemplateView(GenericView):
    queryset = VideoTemplate.objects.all()
    serializer_class = DetailedVideoTemplateSerializer
    allowed_methods = ['retrieve', 'update','delete']


class VideoTemplateView(GenericView):
    queryset = VideoTemplate.objects.all()
    serializer_class = VideoTemplateSerializer
    allowed_methods = ['list', 'create']


class StaticLayerView(GenericView):
    queryset = StaticLayer.objects.all()
    serializer_class = StaticLayerSerializer


class DynamicLayerView(GenericView):
    queryset = DynamicLayer.objects.all()
    serializer_class = DynamicLayerSerializer
