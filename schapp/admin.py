from django.contrib import admin

# Register your models here.

from .models import Profile, DetectedUsers 


admin.site.register(DetectedUsers)
admin.site.register(Profile)