from django.contrib import admin
from django.contrib.auth.models import User,Group

from .models import Course,Category


admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("title","category","price","duration_calc")
    search_fields=("title","category__name","category")
    list_filter = ("category","level","location","price")
    readonly_fields=("created_at",)
    fieldsets=(("General Information",{"fields":("title","category","picture","created_at")}),
               ("Specification Information",{"fields":("location","level","duration_weeks","duration_months",
               "price")}),
               ("Course Details",{"fields":("description","prerequisites","learned_topics")}))
    
    def duration_calc(slef,obj):
        s=""
        if obj.duration_months:
            s=s+str(obj.duration_months)+" month"
            if obj.duration_months>1:
                s=s+"s " 
        if obj.duration_weeks:
            s=s+str(obj.duration_weeks)+" week"
            if obj.duration_weeks>1:
                s=s+"s"
        return s 
    def save_model(self, request, obj, form, change):
        if change==True:
            old_obj=Course.objects.get(id=obj.id)
            if "picture" in request.FILES and old_obj.picture.name!=obj.picture.name :
                old_obj.picture.delete(save=False)        
        return super().save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        obj.picture.delete(save=False)
        return super().delete_model(request, obj)           
admin.site.register(Category)
