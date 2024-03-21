from django.urls import path
from .views import FoodTruckList

urlpatterns = [
    path('', FoodTruckList.as_view(), name='food_trucks'),
]