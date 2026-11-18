from django.shortcuts import get_object_or_404
from .models import Course,Category
from django.db.models import Q

def get_course(id):
    queryset=get_object_or_404(Course,id=id)
    return queryset


def get_courses(search=None,limit=None,category=None):
    queryset=Course.objects.all()
    if search:
        queryset= queryset.filter(Q(title__icontains=search)
        | Q(category__name__icontains=search)
        | Q(description__icontains=search))
    if category:
        queryset = queryset.filter(category__name=category)
    if limit :
        queryset=queryset[:int(limit)]
    return queryset

def get_categories():
    queryset=Category.objects.all()
    return queryset
