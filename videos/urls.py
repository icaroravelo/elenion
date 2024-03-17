from django.urls import path
from . import views

urlpatterns = [
    path('videos', views.videoPage, name='video'),
]
