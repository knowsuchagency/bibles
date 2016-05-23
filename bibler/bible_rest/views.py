from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BibleVerse
from .serializers import BibleVerseSerializer


@api_view(['GET'])
def verse_list(request, format=None):
    """
    List all verses.
    """

    if request.method == 'GET':
        verses = BibleVerse.objects.all()
        serializer = BibleVerseSerializer(verses, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def verse_detail(request, pk, format=None):
    """
    :param request:
    :param pk:
    :return: bible verse
    """

    try:
        verse = BibleVerse.objects.get(pk=pk)
    except BibleVerse.DoesNotExist:
        serializer = BibleVerseSerializer()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = BibleVerseSerializer(verse)
        return Response(serializer.data)
    else:
        serializer = BibleVerseSerializer()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)