from django.urls import path
from . import views as main_app


urlpatterns = [
    path("", main_app.index, name='main_page'),
    path("suggestions", main_app.suggestions, name='suggestions'),
    path("favorites", main_app.favorites, name='favorites'),
    path("item/<int:pk>", main_app.item, name='item'),
]
