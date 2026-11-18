from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SchoolSerializer
from .selectors import get_school

class SchoolDetailAPIView(APIView):
    def get(self,request):
        school=get_school()
        serializer=SchoolSerializer(school)
        return Response(serializer.data)


        