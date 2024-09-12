# videos/urls.py
from django.urls import path
from . import views  # Import views from your own app, not from django

urlpatterns = [
    path('', views.upload_video, name='upload_video'),  # No parentheses
    path('videos/', views.video_list, name='video_list'),
]
