from django.core.management.base import BaseCommand
from FoodTruckSF.models import FoodTruck
import pandas as pd
from django.contrib.gis.geos import Point
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Import food trucks from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Read the CSV file
        df = pd.read_csv(csv_file)

        # Iterate through the DataFrame and create FoodTruck instances
        for _, row in df.iterrows():
            location_point = Point(row['longitude'], row['latitude'])

            # Handle datetime fields
            approved_datetime = parse_datetime(row['approved']) if pd.notnull(row['approved']) else timezone.now()
            expiration_datetime = parse_datetime(row['expiration_date']) if pd.notnull(row['expiration_date']) else timezone.now()

            FoodTruck.objects.update_or_create(
                location_id=row['locationid'],
                defaults={
                    'applicant': row['applicant'],
                    'facility_type': row['facility_type'],
                    'cnn': row['cnn'],
                    'location_description': row['location_description'],
                    'address': row['address'],
                    'blocklot': row['blocklot'],
                    'block': row['block'],
                    'lot': row['lot'],
                    'permit': row['permit'],
                    'status': row['status'],
                    'food_items': row['food_items'],
                    'x': row['x'],
                    'y': row['y'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude'],
                    'schedule': row['schedule'],
                    'dayshours': row['dayshours'],
                    'noisent': row['noisent'],
                    'approved': approved_datetime,
                    'received': row['received'],
                    'prior_permit': row['prior_permit'],
                    'expiration_date': expiration_datetime,
                    'fire_prevention_districts': row['fire_prevention_districts'],
                    'police_districts': row['police_districts'],
                    'supervisor_districts': row['supervisor_districts'],
                    'zip_codes': row['zip_codes'],
                    'neighborhoods_old': row['neighborhoods_old'],
                    'location': location_point
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported food trucks from CSV'))
