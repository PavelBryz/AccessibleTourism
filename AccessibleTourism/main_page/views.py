import os

import openai
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Place

from dotenv import load_dotenv
import pyttsx3
# Create your views here.


def index(request: WSGIRequest):
    return render(request, 'main_page/index.html')


def suggestions(request: WSGIRequest):
    query = Place.objects.all()
    context = {"places": query}
    return render(request, 'main_page/suggestions.html', context=context)


def favorites(request: WSGIRequest):
    return render(request, 'main_page/favorites.html')


def item(request: WSGIRequest, pk):
    return render(request, 'main_page/item.html')
