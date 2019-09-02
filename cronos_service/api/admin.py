from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(
    Profile,
    list_display=['user', 'device_id'],
    search_fields=['user', 'device_id']
)

admin.site.register(
    Application,
    list_display=['application_name', 'application_type'],
    search_fields=['application_name', 'application_type']
)

admin.site.register(
    Notification,
    list_display=['profile', 'application', 'date', 'time', 'count'],
    search_fields=['profile', 'application', 'date', 'time', 'count']
)

