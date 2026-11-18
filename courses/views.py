from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CourseListSerializer,CourseDetailSerializer,CategorySerializer
from .selectors import get_course,get_courses,get_categories


class CourseDetailsAPIView(APIView):
    def get(self,request, id): 
        course=get_course(id)
        serializer=CourseDetailSerializer(course)
        return Response(serializer.data)
class CourseListAPIView(APIView):
    def get(self,request):
        search=request.query_params.get("search")
        limit=request.query_params.get("limit")
        category=request.query_params.get("category")
        if limit is not None:
            try:
                limit = int(limit)
            except ValueError:
                return Response({ "detail": "limit must be an integer."},status=status.HTTP_400_BAD_REQUEST)

        courses=get_courses(search=search,limit=limit,category=category)
        serializer=CourseListSerializer(courses,many=True)
        return Response(serializer.data)
    
class CategoryListAPIView(APIView):
    def get(self,request):
        categories=get_categories()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
        
    