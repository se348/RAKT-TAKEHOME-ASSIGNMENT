# Food Truck Finder

## Description
This is a platform that helps individuals at a specific location looks for food trucks nearby. There are 3 ways to get to access n nearest food trucks. It has been tested with food trucks in San Francisco, US.

## Installation
The first step is to clone the git repository
```
git clone https://github.com/se348/RAKT-TAKEHOME-ASSIGNMENT.git
```

The second step is to install the libraries
```
pip install -r requirements.txt
```

Eventhough there is a default DB connection setup, you can change it in FoodTruckExplore/FoodTruckExplore/settings.py. If you do that you would have to run a command,

```
python .\FoodTruckExplore\manage.py import_food_trucks csv_file
```
to import the file to the mongo database.

The final step is to run 
```
python .\FoodTruckExplore\manage.py runserver
```

## Usage

You can access the food trucks using 3 ways
1. Using CLI
    ```
    python .\FoodTruckExplore\manage.py get_closest_trucks --latitude=50.0 --longitude=30 --limit=10
    ```
    Latitude and longitude are required fields
    Limit is optional
2. Accessing JSON
    ```
    http://localhost:8000?is_json=true
    ```
    Query parameters
    ```
    latitude -> optional, current location latitude
    longitude -> optional, current location longitude
    page -> optional, current page
    page size -> optional, page size
    status -> optional, status of the food truck
    ```
    Sample Response
    ```
    {
    "data": [
            {
                "applicant": "Leo's Hot Dogs",
                "facility_type": "Push Cart",
                "address": "2301 MISSION ST",
                "status": "APPROVED",
                "food_items": "Hot dogs and related toppings: non alcoholic beverages",
                "latitude": 37.76008693198698,
                "longitude": -122.41880648110114,
                "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00008&ExportPDF=1&Filename=23MFF-00008_schedule.pdf",
                "approved": "2024-03-23T07:46:37.356000Z",
                "expiration_date": "2024-03-23T07:46:37.356000Z",
                "id": 1728067
            },
          
            {
                "applicant": "BOWL'D ACAI, LLC.",
                "facility_type": "Truck",
                "address": "200 LARKIN ST",
                "status": "REQUESTED",
                "food_items": "Acai Bowls: Smoothies: Juices",
                "latitude": 37.78021548028814,
                "longitude": -122.41602577015111,
                "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00048&ExportPDF=1&Filename=23MFF-00048_schedule.pdf",
                "approved": "2024-03-23T07:46:41.842000Z",
                "expiration_date": "2024-03-23T07:46:41.842000Z",
                "id": 1744303
            },
            {
                "applicant": "MOMO INNOVATION LLC",
                "facility_type": "Truck",
                "address": "351 CALIFORNIA ST",
                "status": "APPROVED",
                "food_items": "Noodles: Meat & Drinks",
                "latitude": 37.792870749741496,
                "longitude": -122.4007474940767,
                "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00027&ExportPDF=1&Filename=23MFF-00027_schedule.pdf",
                "approved": "2024-03-23T07:46:42.203000Z",
                "expiration_date": "2024-03-23T07:46:42.203000Z",
                "id": 1733728
            },
            {
                "applicant": "MOMO INNOVATION LLC",
                "facility_type": "Truck",
                "address": "101 CALIFORNIA ST",
                "status": "APPROVED",
                "food_items": "MOMO Spicy Noodle: POPO's Noodle: Spicy Chicken Noodle: Rice Noodles",
                "latitude": 37.792948952834664,
                "longitude": -122.39809861316652,
                "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00029&ExportPDF=1&Filename=23MFF-00029_schedule.pdf",
                "approved": "2024-03-23T07:46:42.585000Z",
                "expiration_date": "2024-03-23T07:46:42.585000Z",
                "id": 1733788
            },
            {
                "applicant": "Buenafe",
                "facility_type": "Truck",
                "address": "220 RANKIN ST",
                "status": "APPROVED",
                "food_items": "Tacos: Burritos: Quesadillas: Tortas",
                "latitude": 37.74574924062031,
                "longitude": -122.3924814876784,
                "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00025&ExportPDF=1&Filename=23MFF-00025_schedule.pdf",
                "approved": "2024-03-23T07:46:42.886000Z",
                "expiration_date": "2024-03-23T07:46:42.886000Z",
                "id": 1733610
            }
        ],
        "page": 1,
        "page_size": 10,
        "total": 447,
        "prev_page": null,
        "next_page": 2
    }
    ```
    Accessing Individual Food Truck
    ```
    http://localhost:8000/1733788?is_json=true
    ```
    Sample Response
    ```
    {
        "applicant": "MOMO INNOVATION LLC",
        "facility_type": "Truck",
        "address": "101 CALIFORNIA ST",
        "status": "APPROVED",
        "food_items": "MOMO Spicy Noodle: POPO's Noodle: Spicy Chicken Noodle: Rice Noodles",
        "latitude": 37.792948952834664,
        "longitude": -122.39809861316652,
        "schedule": "http://bsm.sfdpw.org/PermitsTracker/reports/report.aspx?title=schedule&report=rptSchedule&params=permit=23MFF-00029&ExportPDF=1&Filename=23MFF-00029_schedule.pdf",
        "approved": "2024-03-23T07:46:42.585000Z",
        "expiration_date": "2024-03-23T07:46:42.585000Z",
        "id": 1733788
    }
    ```
3. Thorugh Django Template Engine
 Getting List of food trucks
![image](https://github.com/se348/RAKT-TAKEHOME-ASSIGNMENT/assets/66954610/c4bb5f99-f7bd-4710-ae99-ddf2459a783d)
![Screenshot 2024-03-23 135251](https://github.com/se348/RAKT-TAKEHOME-ASSIGNMENT/assets/66954610/d1f262a4-3588-4744-9bdc-752b582e0860)

 Getting Individual food truck 
![Screenshot 2024-03-23 134652](https://github.com/se348/RAKT-TAKEHOME-ASSIGNMENT/assets/66954610/8547531e-891b-49a2-93a9-119671cc5a31)
![image](https://github.com/se348/RAKT-TAKEHOME-ASSIGNMENT/assets/66954610/5bbd2dac-1082-4034-b653-91e3166a5771)

## Tests
For runnning test on views
```
cd FoodTruckExplore
python manage,py test
```

For running test on utils
```
cd FoodTruckExplore
pytest
```

## Liscence

The Assignment is part of the take home exam from RAKT Technologies. The implementation is fully done by Semir Ahmed.///

## Contact

For any opinion please feel free to contact me using my email (semir2578@gmail.com)
