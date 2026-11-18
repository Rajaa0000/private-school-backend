from rest_framework import serializers
from .models import Course,Category

class CourseDetailSerializer (serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model=Course
        fields=[
            "id",
    "title",
    "category",
    "location",
    "level",
    "price",
    "picture",
    "description",
    "prerequisites",
    "learned_topics",
    "duration_weeks",
    "duration_months",

]

class CourseListSerializer (serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    class Meta:
        model=Course
        fields=[
            "id",
    "title",
    "category",
    "location",
    "level",
    "price",
    "picture",
    "duration_weeks",
    "duration_months",
]
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name"]