from django.urls import path 
from . import views
urlpatterns=[
    path("<int:id>/",views.EventDetailsAPIView.as_view(),name="event-details"),
    path("",views.EventListAPIView.as_view(),name="event-list"),
   
]