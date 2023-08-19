from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def index(request: WSGIRequest):
    return render(request, 'main_page/index.html')