from rest_framework import filters, viewsets
from django.views.generic import ListView
from .models import BibleVerse
from .serializers import BibleVerseSerializer


class VerseViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Bible Verses
    ___
    parameters:
        - name: version
          paramType: query
          description: The version of the bible i.e. NIV, ESV, MSG
          type: string
        - name: book
          type: string
          description: Book i.e. Genesis, Judges, Luke
        - name: chapter
          type: integer
        - name: verse
          type: integer

    """
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('version', 'book', 'chapter', 'verse')
    ordering_fields = ('version', 'book', 'chapter', 'verse')
    search_fields = ('text',)


class VerseList(ListView):
    model = BibleVerse