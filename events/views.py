from rest_framework.views import APIView
from rest_framework.response import Response
from .selectors import get_event,get_events
from .serializers import EventDetailSerializer,EventListSerializer

class EventDetailsAPIView( APIView):
    def get(self,request,id):
        event=get_event(id=id)
        serializer=EventDetailSerializer(event)
        return Response(serializer.data)
class EventListAPIView(APIView):
    def get(self,request):
        limit=request.query_params.get("limit")
        events=get_events(limit=limit)
        serializer=EventListSerializer(events,many=True)
        return Response(serializer.data)