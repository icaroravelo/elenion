from django.shortcuts import render, redirect, get_object_or_404
from .models import New, Member, About, Album
from django.http import HttpResponse
from videos.models import Video

# Create your views here.
def homePage(request):
    # Most recent news to return into the homepage
    recent_news = New.objects.order_by('-original_released_date')[:1]

    # Call the latest video from the app 'Videos' to homepage 
    videos = Video.objects.all()[:1]

    # Get the latest album
    latest_album = Album.objects.order_by('-released_at')[:1]

    # Pass the news to the template
    context = {'news' : recent_news, 'videos': videos, 'albums': latest_album}

    return render (request, 'pages/home.html', context)

def aboutPage(request):
    infos = About.objects.all()
    context = {'infos' : infos}
    return render(request, 'pages/about.html', context)

def newsPage(request):
    news = New.objects.all()
    context = {'news' : news}
    return render(request, 'pages/news.html', context)

def membersPage(request):
    members = Member.objects.all()
    context = {'members' : members}
    return render(request, 'pages/members.html', context)

def privacyPage(request):
    return render(request, 'pages/privacy.html')

def individual_new(request, slug):
    # Retrieve the specific news article with the given slug
    new = get_object_or_404(New, slug=slug)
    
    # Pass only the specific news article to the template
    context = {'new': new}
    
    return render(request, 'pages/individual_new.html', context)