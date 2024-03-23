// static/js/foodTruckMap.js

function initializeMap(latitude, longitude, applicant, address) {
    var map = L.map('map').setView([latitude, longitude], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    L.marker([latitude, longitude]).addTo(map)
        .bindPopup(`<b>${applicant}</b><br>${address}`).openPopup();
}
