from django.urls import path, include
import django_twilio

from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('video/<str:stream_path>',dynamic_stream, name="videostream"),  
    path('registration', registration, name="registration"),
    path('observation-gelen', observation_gelen, name="observation-gelen"),
    path('observation-gelmedik', observation_gelmedik, name="observation-gelmedik"),
    path('detected-users', detected_user, name="detected-users"),
    path('unknown-users', unknown_user, name="unknown-users"),
    path('unknown-users-analysis', unknown_user_analysis, name="unknown-users-analysis"),
    path('known-users-analysis/<int:value>', known_user_analysis, name="known-users-analysis"),
    path('gelmedik-analysis/<int:value>', gelmedik_analysis, name="gelmedik-analysis"),
    path('unknown-users-delete/<str:path>', unknown_user_delete, name="unknown-users-delete"),
    path('known-users-delete/<str:id>', known_user_delete, name="known-users-delete"),
    path('registration-time', registration_time, name="registration-time"),
    path('camera-changer', camera_changer, name="camera-changer"),
] 