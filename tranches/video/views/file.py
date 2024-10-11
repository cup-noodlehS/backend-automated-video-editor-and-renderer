from tranches.utils.generic_api import GenericView

from video.models import File, Font, AeVersion
from video.serializers import FileSerializer, FontSerializer, AeVersionSerializer


class FileView(GenericView):
    queryset = File.objects.all()
    serializer_class = FileSerializer