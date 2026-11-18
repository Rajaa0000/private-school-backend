from django.shortcuts import get_object_or_404
from .models import Event
def get_event(id):
    queryset = get_object_or_404(Event,id=id)
    return queryset
def get_events(limit=None):
    queryset = Event.objects.all()
    if limit :
        queryset=queryset[:int(limit)]
    return queryset

