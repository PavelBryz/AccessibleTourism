from django.db import models
from django.conf import settings


# Create your models here.

class Requirements(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    public_toilet = models.BooleanField("public_toilet", default=False)
    walking_stick = models.BooleanField("accessible_by_walking_stick", default=False)
    wheel_chair = models.BooleanField("accessible_by_wheel_chair", default=False)
    wheel_chair_with_help = models.BooleanField("accessible_by_wheel_chair_with_help", default=False)
    priority_parking = models.BooleanField("priority_parking", default=False)
    mobility_impairment_facilities = models.BooleanField("mobility_impairment_facilities", default=False)
    visual_impairment_facilities = models.BooleanField("visual_impairment_facilities", default=False)
