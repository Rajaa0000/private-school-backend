from rest_framework import serializers
from .models import School

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=[
    "name",
    "logo",
    "description",
    "email",
    "phone",
    "address",
    "instagram",
    "facebook",
    "linkedin",
    "maps",
    "link_to_enroll",
]