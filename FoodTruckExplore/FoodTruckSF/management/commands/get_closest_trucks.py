from django.core.management.base import BaseCommand
from FoodTruckSF.serializer import FoodTruckSerializer
from FoodTruckSF.models import FoodTruck 

class Command(BaseCommand):
    '''
    Get the closest food trucks to a given location.
    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        limit (int): The maximum number of food trucks to return.
    '''
    help = 'Get the closest food trucks to a given location.'

    def add_arguments(self, parser):
        parser.add_argument('--latitude', type=float, help='The latitude of the location.', required=True)
        parser.add_argument('--longitude', type=float, help='The longitude of the location.', required=True)
        parser.add_argument('--limit', type=int, help='The maximum number of food trucks to return.', default=5)

    def handle(self, *args, **kwargs):
        latitude = kwargs['latitude']
        longitude = kwargs['longitude']
        limit = kwargs['limit']
        
        latitude = float(latitude)
        longitude = float(longitude)
        limit = int(limit)
        self.stdout.write(f'Getting the closest food trucks to location ({latitude}, {longitude})\n')

        pipeline = [
            {
                '$geoNear': {
                    'near': {'type': "Point", 'coordinates': [longitude, latitude]},
                    'distanceField': "distance",
                    'spherical': True
                }
            },
            {
                '$limit': limit
            }
        ]

        # Execute the pipeline
        queryset = FoodTruck.objects.aggregate(*pipeline)
        serializer = FoodTruckSerializer(list(queryset), many=True)

        self.stdout.write(f'Closest food trucks to location ({latitude}, {longitude}): ')
        for data in serializer.data:
            self.stdout.write(f'Food Truck: {data["applicant"]}, Distance: {data["distance"]}, Address: {data["address"]}, location: {data["latitude"]} {data["longitude"]}')
        
