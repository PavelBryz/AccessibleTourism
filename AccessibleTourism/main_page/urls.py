from django.urls import path
from . import views as main_app


urlpatterns = [
    path("", main_app.index, name='main_page'),
]
