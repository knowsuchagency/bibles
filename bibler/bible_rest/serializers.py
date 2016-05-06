from .models import *
from rest_framework import serializers

class BibleVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BibleVersion
        fields = ('id', 'name')
