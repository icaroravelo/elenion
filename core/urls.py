from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('news/', views.newsPage, name='news'),
    path('news/<slug>/', views.individual_new, name='individual_new'),
    path('members/', views.membersPage, name='members'),
    path('about/', views.aboutPage, name='about'),
    path('privacy/', views.privacyPage, name='privacy'),
]
