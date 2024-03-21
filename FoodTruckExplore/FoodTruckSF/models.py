from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models

class FoodTruck(models.Model):
    location_id = models.BigIntegerField(primary_key=True)
    applicant = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100)
    cnn = models.BigIntegerField()
    location_description = models.TextField()
    address = models.CharField(max_length=255)
    blocklot = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    lot = models.CharField(max_length=50)
    permit = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    food_items = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    schedule = models.URLField(max_length=1024)
    dayshours = models.CharField(max_length=255, blank=True, null=True)
    noisent = models.CharField(max_length=255, blank=True, null=True)
    approved = models.DateTimeField(default=timezone.now())
    received = models.IntegerField()
    prior_permit = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(default=timezone.now())
    fire_prevention_districts = models.IntegerField()
    police_districts = models.IntegerField()
    supervisor_districts = models.IntegerField()
    zip_codes = models.IntegerField()
    neighborhoods_old = models.IntegerField()
    location = gis_models.PointField(geography=True, blank=True, null=True)

    def __str__(self):
        return self.applicant
    
    class Meta:
        verbose_name = "Food Truck"
        verbose_name_plural = "Food Trucks"
        ordering = ['applicant']









        