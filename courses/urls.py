from django.urls import path 
from . import views
urlpatterns=[
    path("<int:id>/",views.CourseDetailsAPIView.as_view(),name="course-details"),
    path("",views.CourseListAPIView.as_view(),name="course-list"),
    path("categories/",views.CategoryListAPIView.as_view(),name="category-list")
]