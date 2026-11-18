from django.db import models

class School(models.Model):

    name=models.CharField(max_length=100)
    
    logo=models.ImageField(upload_to="school/")
    description=models.TextField(blank=True)

    email=models.EmailField()
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=200)


    instagram=models.URLField(blank=True)
    facebook=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    maps=models.URLField(blank=True)

    link_to_enroll=models.URLField()

    def __str__(self):
        return  self.name


