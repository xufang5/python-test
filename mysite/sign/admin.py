from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.
#将表映射到admin后台

class EventAdmin(admin.ModelAdmin):
    #展示在admin后台的列
    list_display = ["name","limit","address","start_time"]
    search_fields =["name"]

class GuestAdmin(admin.ModelAdmin):

    list_display = ["realname","phone","email"]
    search_fields =["realname"]

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)
