from rest_framework import generics
from .models import BibleVerse
from .serializers import BibleVerseSerializer


class VerseList(generics.ListAPIView):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer


class VerseDetail(generics.RetrieveAPIView):
    queryset = BibleVerse.objects.all()
    serializer_class = BibleVerseSerializer