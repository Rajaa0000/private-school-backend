from django.contrib import admin
from .models import School
@admin.register(School)
class SchoolAdmin (admin.ModelAdmin):


    list_display=("name","email","phone","address")
    fieldsets=(("General Information",{"fields":("name","logo","description")}),
               ("Contact Information",{"fields":("email","phone","address","link_to_enroll")}),
               ("Links/Social Media Information",{"fields":("instagram","facebook","linkedin","maps")}))
   
    def has_delete_permission(self, request,obj=None):
        return not School.objects.all()
    def has_add_permission(self, request,obj=None):
        return  not School.objects.all()

    def save_model(self, request, obj, form, change):#notice that the obj is already the new like obj with the new data 
        old_obj=School.objects.first()
        if change==True:
            if "logo" in  request.FILES and obj.logo.name!=old_obj.logo.name:
                old_obj.logo.delete(save=False)
        return super().save_model(request, obj, form, change)