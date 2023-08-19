import os

import openai
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from dotenv import load_dotenv
import pyttsx3
# Create your views here.


def index(request: WSGIRequest):
    return render(request, 'main_page/index.html')


def suggestions(request: WSGIRequest):
    return render(request, 'main_page/suggestions.html')


def favorites(request: WSGIRequest):
    return render(request, 'main_page/favorites.html')


def item(request: WSGIRequest, pk):
    return render(request, 'main_page/item.html')
