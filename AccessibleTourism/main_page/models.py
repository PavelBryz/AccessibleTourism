from django.db import models
from django.conf import settings


# Create your models here.

class Place(models.Model):
    name = models.CharField('name', max_length=100)
    description = models.CharField('description', max_length=500)
    public_toilet = models.BooleanField("public_toilet", default=True)
    accessible_by_walking_stick = models.BooleanField("accessible_by_walking_stick", default=False)
    accessible_by_wheel_chair = models.BooleanField("accessible_by_wheel_chair", default=False)
    accessible_by_wheel_chair_with_help = models.BooleanField("accessible_by_wheel_chair_with_help", default=False)
    priority_parking = models.BooleanField("priority_parking", default=False)
    mobility_impairment_facilities = models.BooleanField("mobility_impairment_facilities", default=False)
    visual_impdairment_facilities = models.BooleanField("visual_impairment_facilities", default=True)

    def __str__(self):
        return f"{self.name} | {self.description}"


class GlobalRating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.place} | {self.rating}"


class Rating(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    rating = models.IntegerField('rating')

    def __str__(self):
        return f"{self.place} | {self.user} | {self.rating}"


class Favorites(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    favorite = models.BooleanField("favorite")

    def __str__(self):
        return f"{self.place} | {self.user} | {self.favorite}"
