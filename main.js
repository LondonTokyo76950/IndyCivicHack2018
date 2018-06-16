var map;
      
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8
    });
}

var broadway = {
    info: '<strong>Chipotle on Broadway</strong><br>\
                5224 N Broadway St<br> Chicago, IL 60640<br>\
                <a href="https://goo.gl/maps/jKNEDz4SyyH2">Get Directions</a>',
    lat: 41.976816,
    long: -87.659916
};