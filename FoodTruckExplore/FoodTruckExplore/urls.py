
from django.urls import path, include

urlpatterns = [
    path('food-trucks/', include('FoodTruckSF.urls')),
]
