from rest_framework import filters, viewsets
from .models import BibleVerse
from .serializers import BibleVerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter,)
    filter_fields = ('version', 'book', 'chapter', 'verse')
    ordering_fields = ('version', 'book', 'chapter', 'verse')
    search_fields = ('text',)