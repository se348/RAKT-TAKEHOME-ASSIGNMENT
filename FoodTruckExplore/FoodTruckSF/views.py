from rest_framework.views import APIView
from .models import FoodTruck
from FoodTruckSF.serializer import FoodTruckSerializer
from rest_framework.response import Response 
from rest_framework import status
from FoodTruckSF.utils import get_prev_and_next_page, paginate_query
from django.shortcuts import render

class FoodTruckDetailView(APIView):
    def get_object(self, _id):
        try:
            return FoodTruck.objects.get(_id=_id)
        except FoodTruck.DoesNotExist:
            return None

    def get(self, request, _id, *args, **kwargs):
        '''
        Get a single food truck by id
        '''
        food_truck = self.get_object(_id)
        if food_truck is None:
            return Response({"message": "FoodTruck not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = FoodTruckSerializer(food_truck)

        # Check if the request is for JSON data
        is_json = request.query_params.get('is_json', "false")
        if is_json.lower() == 'true':
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            context = {'food_truck': serializer.data}
            return render(request, 'food_truck_detail.html', context)

    
class FoodTruckListView(APIView):
    def get_paginated_and_filtered_list(self, request)->list[FoodTruck]:
        '''
        Get a paginated and filtered list of food trucks
        '''
        applicant = request.query_params.get('applicant', None)
        status = request.query_params.get('status', None)

        # Pagination parameters
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 10))

        # Location parameters for sorting
        latitude = request.query_params.get('latitude', None)
        longitude = request.query_params.get('longitude', None)

        # Start building the aggregation pipeline
        pipeline = []

        # Add filtering stages
        if applicant:
            pipeline.append({'$match': {'applicant': {'$regex': applicant, '$options': 'i'}}})
        if status:
            pipeline.append({'$match': {'status': status}})

        # Add sorting by distance if location is provided
        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                pipeline.append({
                    '$geoNear': {
                        'near': {'type': "Point", 'coordinates': [longitude, latitude]},
                        'distanceField': "distance",
                        'spherical': True
                    }
                })
            except ValueError:
                raise ValueError('Invalid latitude or longitude values')
        
        count_result = list(FoodTruck.objects.aggregate(*pipeline, {'$count': 'count'}))
        
        count = count_result[0]["count"] if count_result else 0
        
        # Implement pagination within the pipeline
        skip, limit = paginate_query(page, page_size)
        pipeline.append({'$skip': skip})
        pipeline.append({'$limit': limit})

        # Execute the pipeline
        queryset = FoodTruck.objects.aggregate(*pipeline)
        serializer = FoodTruckSerializer(list(queryset), many=True)

        # Calculate previous and next page numbers
        prev_page, next_page = get_prev_and_next_page(page, page_size, count)
        result = {
            "data": serializer.data, 
            "page": page, 
            "page_size": page_size, 
            "total": count, 
            "prev_page": prev_page, 
            "next_page": next_page
            }
        
        return result
    
    def get(self, request, *args, **kwargs):
        try:
            result = self.get_paginated_and_filtered_list(request)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)
        
        # Check if the request is for JSON data
        is_json = request.query_params.get('is_json', "false")
        if is_json.lower() == 'true':
            return Response(result, status=status.HTTP_200_OK)
        else:
            context = {'results': result}
            return render(request, 'food_truck_list.html', context)
       


