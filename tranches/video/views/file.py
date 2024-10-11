from tranches.utils.generic_api import GenericView

from video.models import File, Font, AeVersion
from video.serializers import FontSerializer, AeVersionSerializer


class FontView(GenericView):
    queryset = Font.objects.all()
    serializer_class = FontSerializer


class AeVersionView(GenericView):
    queryset = AeVersion.objects.all()
    serializer_class = AeVersionSerializer
