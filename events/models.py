from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=100,null=False,unique=True)
    category=models.CharField(max_length=100,null=False)

    start_at=models.DateTimeField(null=False)
    location=models.CharField(max_length=100,default="At School")

    description=models.TextField(default="")
    open_for=models.CharField(max_length=100, default="School Student")
    picture=models.ImageField(null=False,upload_to="events/")
    

    class Meta:
        ordering=["start_at"]

    def __str__(self):
        return self.title
