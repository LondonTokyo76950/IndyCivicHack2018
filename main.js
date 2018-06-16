function initMap() {
	
	var broadway = {
		info: '<strong>Chipotle on Broadway</strong><br>\
					5224 N Broadway St<br> Chicago, IL 60640<br>\
					<a href="https://goo.gl/maps/jKNEDz4SyyH2">Get Directions</a>',
		lat: 41.976816,
		long: -87.659916
	};

	var belmont = {
		info: '<strong>Chipotle on Belmont</strong><br>\
					1025 W Belmont Ave<br> Chicago, IL 60657<br>\
					<a href="https://goo.gl/maps/PHfsWTvgKa92">Get Directions</a>',
		lat: 41.939670,
		long: -87.655167
	};

	var sheridan = {
		info: '<strong>Edna Martin Christian Center</strong><br>\r\
                2605 East 25th Street<br> Indianapolis, IN 46218<br>\
				<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		lat: 39.8029,
        long: -86.11894
    };

	var locations = [
      [broadway.info, broadway.lat, broadway.long, 0],
      [belmont.info, belmont.lat, belmont.long, 1],
      [sheridan.info, sheridan.lat, sheridan.long, 2],
    ];

    var latitude;
    var longitude;
    var geocoder = new google.maps.Geocoder();
    var address = '2605 East 25th Street, Indianapolis, IN 46218';
    geocoder.geocode({ 'address': address }, function (results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
        latitude = results[0].geometry.location.lat();
        longitude = results[0].geometry.location.lng();
        alert("Latitude: " + latitude + "\nLongitude: " + longitude);
        cont(latitude, longitude, locations);
    } else {
        alert("Request failed.")
    }
    });
}

function cont(latitude, longitude, locations) {
    var latFl = parseFloat(latitude).toFixed(7);
    var longFl = parseFloat(longitude).toFixed(7);
    
	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 13,
		center: new google.maps.LatLng(latFl, longFl),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});

	var infowindow = new google.maps.InfoWindow({});

	var marker, i;

	for (i = 0; i < locations.length; i++) {
		marker = new google.maps.Marker({
			position: new google.maps.LatLng(locations[i][1], locations[i][2]),
			map: map
		});

		google.maps.event.addListener(marker, 'click', (function (marker, i) {
			return function () {
				infowindow.setContent(locations[i][0]);
				infowindow.open(map, marker);
			}
		})(marker, i));
	}
}