function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
        getlocation();
    });
    return vars;
}

function getlocation() {
    var address = '2605 East 25th Street, Indianapolis, IN 46218';
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': address }, function (results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
        latitude = results[0].geometry.location.lat();
        longitude = results[0].geometry.location.lng();
        var div1 = document.getElementById("latitude");
        div1.textContent = latitude;
        var div2 = document.getElementById("longitude");
        div2.textContent = longitude;
    } else {
        alert("Request failed.")
    }
    });
}