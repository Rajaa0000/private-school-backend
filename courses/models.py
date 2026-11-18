from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    LOCATIONS=[("onsite","Onsite"),("hybrid","Hybrid"),("online","Online")]
    LEVELS=[("beginner","Beginner"),("intermediate","Intermediate"),("advanced","Advanced")]

    title=models.CharField(max_length=100,null=False,unique=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    location=models.CharField( max_length=20,choices=LOCATIONS,default="onsite")
    level=models.CharField( max_length=20,choices=LEVELS)
    price=models.PositiveIntegerField(null=False)
    picture=models.ImageField(null=False,upload_to="courses/")

    description=models.TextField(default="")
    prerequisites=models.TextField(default="")
    learned_topics=models.TextField(default="")

    duration_weeks=models.PositiveBigIntegerField(null=False)
    duration_months=models.PositiveBigIntegerField(null=False)
    created_at=models.DateField(auto_now_add=True)

    class Meta:
        ordering=["-created_at"]
    def __str__(self):
        return self.title
    def clean(self):
        if self.duration_weeks== self.duration_months==False:
            raise ValidationError(
                "Exactly one of duration_weeks or duration_months must be above zero."
            )
        if self.price==0:
            raise ValidationError("The price should be above 0")

    
