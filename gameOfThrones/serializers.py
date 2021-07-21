from rest_framework import serializers
from .models import Characters

class CharactersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characters
        fields = [
            'pk',
            'id',
            'name',
            'gender',
            'culture',
            'born',
            'died',
            'titles',
            'aliases',
            'father',
            'mother',
            'spouse',
            'allegiances',
            'books',
            'povBooks',
            'tvSeries',
            'playedBy',
        ]
        extra_kwargs = {
            'url': {"required": False}
        }