function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function getlocation() {
    var address = '2605 East 25th Street, Indianapolis, IN 46218';
    geocoder.geocode({ 'address': address }, function (results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
        latitude = results[0].geometry.location.lat();
        longitude = results[0].geometry.location.lng();
        alert("Latitude: " + latitude + "\nLongitude: " + longitude);
        cont(latitude, longitude, locations);
        var div = document.getElementById("coordinates");
        div.textContent = latitude;
    } else {
        alert("Request failed.")
    }
    });
}