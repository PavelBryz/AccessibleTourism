from django.contrib import admin
from .models import Place, GlobalRating, Rating, Favorites

# Register your models here.
admin.site.register(Place)
admin.site.register(GlobalRating)
admin.site.register(Rating)
admin.site.register(Favorites)