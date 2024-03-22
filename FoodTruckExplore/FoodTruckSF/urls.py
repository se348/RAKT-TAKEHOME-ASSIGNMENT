from django.urls import path
from .views import FoodTruckListView, FoodTruckDetailView

urlpatterns = [
    path('', FoodTruckListView.as_view(), name='food_trucks'),
    path('<int:_id>/', FoodTruckDetailView.as_view(), name='food-truck-detail'), 
]