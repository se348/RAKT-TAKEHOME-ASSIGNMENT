from mongoengine import Document, StringField, IntField, FloatField, BooleanField, DateTimeField, URLField, PointField
from django.utils import timezone

class FoodTruck(Document):
    _id = IntField(primary_key=True)
    applicant = StringField(max_length=255, required=True)
    facility_type = StringField(max_length=100)
    cnn = IntField(default=0)
    location_description = StringField()
    address = StringField(max_length=255)
    blocklot = StringField(max_length=50)
    block = StringField(max_length=50)
    lot = StringField(max_length=50)
    permit = StringField(max_length=50)
    status = StringField(max_length=100)
    food_items = StringField()
    x = FloatField()
    y = FloatField()
    latitude = FloatField()
    longitude = FloatField()
    schedule = URLField(max_length=1024)
    dayshours = StringField(max_length=255, null=True)    
    noisent = StringField(max_length=255, null=True)
    approved = DateTimeField(default=timezone.now)
    received = IntField(default=0)
    prior_permit = BooleanField(default=False)
    expiration_date = DateTimeField(default=timezone.now)
    fire_prevention_districts = IntField(default=0)
    police_districts = IntField(default=0)
    supervisor_districts = IntField(default=0)
    zip_codes = IntField(default=0)
    neighborhoods_old = IntField(default=0)
    location = PointField(auto_index=False, required=True)

    meta = {
        'collection': 'food_trucks',  # MongoDB collection name
        'ordering': ['applicant']
    }