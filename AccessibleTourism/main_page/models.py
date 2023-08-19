from django.db import models

# Create your models here.

class Place(models.Model):
    name                = models.CharField( max_length=500)
    public_toilet       = models.BooleanField("pub")
    very_steep = models.BooleanField("pub")
    priority_parking    = models.BooleanField("pub")
    mobility_impairment_facilities = models.booleanooleanField("pub")
    visual_impairment_facilities = models.Boolean("pub")
    facilities_found_here = models.CharField( max_length=500 )
    accessibility_information = models.CharField( max_length=500)

class Rating():
     Place = models.ForeignKey(Place)
     rating = models.FloatField(min=0.0, max=5.0)

