from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here.
def videoPage(request):
    videos = Video.objects.all()
    context = {'videos' : videos}
    return render(request, context)