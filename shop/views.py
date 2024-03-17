from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def shopPage(request):
    return HttpResponse('Shop page is working!')