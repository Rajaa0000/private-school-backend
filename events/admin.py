from django.contrib import admin 
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields=[
    "title",
    "category",
    "start_at",
    "location",
    "description",
    "open_for",
    "picture",
]
    list_display=("title","category","start_at","location","open_for")
    list_filter=("category","location","start_at","open_for")
    search_fields=("title","category","location","open_for")
    def save_model(self, request, obj, form, change):

        if change==True:
            old_obj=Event.objects.get(id=obj.id)
            if "picture" in request.FILES and old_obj.picture.name!=obj.picture.name :
                old_obj.picture.delete(save=False)

        return super().save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        obj.picture.delete(save=False)
        return super().delete_model(request, obj)

    

