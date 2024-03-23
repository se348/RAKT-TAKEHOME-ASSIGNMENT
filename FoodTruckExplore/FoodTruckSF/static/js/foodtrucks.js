document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('findNearbyTrucks').addEventListener('click', function() {
        document.getElementById('findNearbyTrucks').textContent = `Loading...`;
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                document.getElementById('findNearbyTrucks').textContent = `Find Nearby Food Trucks`;
                // Display latitude and longitude
                document.getElementById('locationInfo').textContent = `Latitude: ${latitude}, Longitude: ${longitude}`;
                 // Update the URL with latitude and longitude as query parameters
                 const newUrl = new URL(window.location.href);
                 newUrl.searchParams.set('latitude', latitude);
                 newUrl.searchParams.set('longitude', longitude);
 
                 // Update browser history with new URL
                 window.location.href = newUrl;
            }, function(error) {
                alert('Error getting location: ' + error.message);
            });
        } else {
            alert('Geolocation is not supported by your browser.');
        }
    });
});
