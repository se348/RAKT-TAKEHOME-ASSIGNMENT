from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import FoodTruck
from .serializers import FoodTruckSerializer  

class FoodTruckList(APIView):
    def get(self, request, format=None):
        food_trucks = FoodTruck.objects.all().order_by('applicant')  
        paginator = PageNumberPagination()
        paginator.page_size = 2  
        result_page = paginator.paginate_queryset(food_trucks, request)
        serializer = FoodTruckSerializer(result_page, many=True)
        data = serializer.data
        return Response({
            'count': paginator.page.paginator.count,
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
            'results': data
        })
