from rest_framework import serializers
from .models import Event

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=[
            "id",
    "title",
    "category",
    "start_at",
    "location",
    "description",
    "open_for",
    "picture",
]

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=[
            "id",
    "title",
    "category",
    "start_at",
    "location",
    "picture",
]