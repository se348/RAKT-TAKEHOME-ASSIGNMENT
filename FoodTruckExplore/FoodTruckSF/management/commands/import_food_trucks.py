import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from FoodTruckSF.models import FoodTruck

class Command(BaseCommand):
    '''
    Import food trucks data from a CSV file into MongoDB.
    Args:
        csv_filename (str): The filename of the CSV to import.
    '''
    help = 'Import food trucks data from a CSV file into MongoDB.'

    def add_arguments(self, parser):
        # Positional argument for the CSV file name
        parser.add_argument('csv_filename', type=str, help='The filename of the CSV to import.')

    def handle(self, *args, **kwargs):
        csv_filename = kwargs['csv_filename']  # Get the CSV filename argument

        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    food_truck = FoodTruck(
                        _id=int(row['locationid']),
                        applicant=row['applicant'],
                        facility_type=row['facility_type'],
                        cnn=int(row['cnn']) if row['cnn'] else None,
                        location_description=row['location_description'],
                        address=row['address'],
                        blocklot=row['blocklot'],
                        block=row['block'],
                        lot=row['lot'],
                        permit=row['permit'],
                        status=row['status'],
                        food_items=row['food_items'],
                        x=float(row['x']) if row['x'] else None,
                        y=float(row['y']) if row['y'] else None,
                        latitude=float(row['latitude']) if row['latitude'] else None,
                        longitude=float(row['longitude']) if row['longitude'] else None,
                        schedule=row['schedule'],
                        dayshours=row['dayshours'],
                        noisent=row['noisent'],
                        approved=parse_datetime(row['approved']),
                        received=int(row['received']) if row['received'] else None,
                        prior_permit=bool(row['prior_permit']),
                        expiration_date=parse_datetime(row['expiration_date']),
                        fire_prevention_districts=int(row['fire_prevention_districts']),
                        police_districts=int(row['police_districts']),
                        supervisor_districts=int(row['supervisor_districts']),
                        zip_codes=int(row['zip_codes']),
                        neighborhoods_old=int(row['neighborhoods_old']),
                        location={'type': 'Point', 'coordinates': [float(row['longitude']),  float(row['latitude'])]} if row['longitude'] and row['latitude'] else None,
                    )
                    food_truck.save()
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error importing row: {e}'))

            self.stdout.write(self.style.SUCCESS('Successfully imported food trucks data from {}.'.format(csv_filename)))
