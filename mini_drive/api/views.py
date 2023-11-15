from rest_framework import viewsets
from api.serializers import TextFileSerializer
from files.models import TextFile


class TextFileViewset(viewsets.ModelViewSet):
    queryset = TextFile.objects.all()
    serializer_class = TextFileSerializer
