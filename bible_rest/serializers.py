from .models import BibleVerse
from rest_framework import serializers


class BibleVerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleVerse
        fields = ('id', 'version', 'book', 'chapter', 'verse', 'text')
