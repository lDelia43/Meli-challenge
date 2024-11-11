# myapi/serializers.py
from rest_framework import serializers
from .models import Item

class DnaSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'