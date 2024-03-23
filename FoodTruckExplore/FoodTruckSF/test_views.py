import unittest
from unittest.mock import patch, MagicMock
from FoodTruckSF.views import FoodTruckListView


side_effects = [
            [{'count': 2}],
            [{
            "_id": 23,
            "applicant": "Some Applicant", "status": "Approved", 
            "latitude": 37.7749295, "longitude": -122.4194155, 
            "approved": "2020-01-01T00:00:00Z", "expiration_date": "2020-01-01T00:00:00Z", 
            "distance": 0.0, "schedule": "http://schedule.test", 
            "food_items": "Pizza, Pasta", "facility_type": "Truck", 
            "address": "1234 Main St", "cnn": 123456, "location_description": "Near the park", 
            "blocklot": "1234", "block": "1234", "lot": "1234", "permit": "1234", 
            "dayshours": "Mon-Fri: 9AM-5PM", "noisent": "1234", "received": 1234,
            "prior_permit": False, 
            "fire_prevention_districts": 1, "police_districts": 1, "supervisor_districts": 1, 
            "zip_codes": 1, "neighborhoods_old": 1, "location": {"type": "Point", "coordinates": [-122.4194155, 37.7749295]}}]]

serializer_return_value =  [{
            '_id': 1,
            'applicant': 'Some Applicant',
            'facility_type': 'Truck',
            'address': "1234 Main St",
            'status': 'Approved',
            'food_items': 'Test Food',
            'latitude': 37.7749295,
            'longitude': -122.4194155,
            'schedule': 'http://schedule.test',
            'approved': '2020-01-01T00:00:00Z',
            'expiration_date': '2020-01-01T00:00:00Z',
            'distance': 0.5
}]

class TestFoodTruckView(unittest.TestCase):        

    @patch('FoodTruckSF.views.FoodTruck.objects.aggregate')
    @patch('FoodTruckSF.views.FoodTruckSerializer')
    def test_get_paginated_and_filtered_list(self, mock_serializer, mock_aggregate):
        # Setup mock request with query parameters
        mock_request = MagicMock()
        mock_request.query_params = {
            'applicant': 'Some Applicant',
            'status': 'Approved',
            'page': '1',
            'page_size': '10'
        }

        # Mock the database aggregation result
        mock_aggregate.side_effects = side_effects
        mock_serializer.return_value.data = serializer_return_value
        # Mock the serializer to return expected data format
        # mock_serializer.return_value.data = [{'applicant': 'Some Applicant', 'status': 'Approved'}]

        # Instantiate the view and call the method
        view_instance = FoodTruckListView()
        result = view_instance.get_paginated_and_filtered_list(mock_request)

        # Assertions to verify the behavior
        self.assertIsNotNone(result)
        self.assertIn('data', result)
        self.assertEqual(len(result['data']), 1)
        self.assertEqual(result['data'][0]['applicant'], 'Some Applicant')
        self.assertEqual(result['page'], 1)
        self.assertEqual(result['page_size'], 10)

        # Ensure the aggregate method was called with the expected pipeline
        # You can add more specific assertions here to check the pipeline arguments

    @patch('FoodTruckSF.views.FoodTruck.objects.aggregate')
    @patch('FoodTruckSF.views.FoodTruckSerializer')
    def test_get_paginated_and_filtered_list_with_location(self, mock_serializer, mock_aggregate):
        # Setup mock request with query parameters
        mock_request = MagicMock()
        mock_request.query_params = {
            'latitude': '37.7749295',
            'longitude': '-122.4194155',
            'page': '1',
            'page_size': '10'
        }

        # Mock the database aggregation result
        mock_aggregate.side_effects = side_effects
        mock_serializer.return_value.data = serializer_return_value
        view_instance = FoodTruckListView()
        result = view_instance.get_paginated_and_filtered_list(mock_request)

        self.assertIsNotNone(result)
        self.assertIn('data', result)
        self.assertEqual(len(result['data']), 1)
        self.assertIsNotNone(result['data'][0]['distance'])
        self.assertEqual(result['data'][0]['distance'], 0.5)

