from .models import School

def get_school():
    queryset=School.objects.all().first()
    return queryset
