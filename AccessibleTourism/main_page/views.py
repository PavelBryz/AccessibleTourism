import os

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Place

from dotenv import load_dotenv
import pyttsx3
# Create your views here.


def index(request: WSGIRequest):
    return render(request, 'main_page/index.html')


def suggestions(request: WSGIRequest):
    query = Place.objects.values('id',
                                 'name',
                                 'description',
                                 'public_toilet',
                                 'accessible_by_walking_stick',
                                 'accessible_by_wheel_chair',
                                 'priority_parking',
                                 'visual_impdairment_facilities',
                                 'rating__rating',
                                 'favorites__favorite')
    context = {"places": query}
    return render(request, 'main_page/suggestions.html', context=context)


def favorites(request: WSGIRequest):
    query = Place.objects.values('id',
                                 'name',
                                 'description',
                                 'public_toilet',
                                 'accessible_by_walking_stick',
                                 'accessible_by_wheel_chair',
                                 'priority_parking',
                                 'visual_impdairment_facilities',
                                 'rating__rating',
                                 'favorites__favorite',
                                 'favorites__user__id',).filter(favorites__user__id=request.user.id, favorites__favorite=True)
    context = {"places": query}
    return render(request, 'main_page/suggestions.html', context=context)


def item(request: WSGIRequest, pk):
    query = Place.objects.values('id',
                                 'name',
                                 'description',
                                 'public_toilet',
                                 'accessible_by_walking_stick',
                                 'accessible_by_wheel_chair',
                                 'priority_parking',
                                 'visual_impdairment_facilities',
                                 'rating__rating',
                                 'favorites__favorite').get(id=pk)
    return render(request, 'main_page/item.html', context={'place': query})
