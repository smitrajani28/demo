from django.contrib import admin
from service2.models import service,savedata

class serviceAdmin(admin.ModelAdmin):
    display_list = ('service_title','service_desc','image_field')

admin.site.register(service,serviceAdmin)

class savedataAdmin(admin.ModelAdmin):
    display_list = ('name','email','number','address')
admin.site.register(savedata,savedataAdmin)
# Register your models here.
