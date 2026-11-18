from django.urls import path
from .views import SchoolDetailAPIView

urlpatterns=[path("",SchoolDetailAPIView.as_view(),name="school-detail")]