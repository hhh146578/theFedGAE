
/*
  ========================================
  ****Hung-Wen Chen  contribution – SI 539****
  Google Map 
  ========================================
*/

var map;
var newMarker;
function initMap() {
	var mapDiv = document.getElementById('map');
	var map = new google.maps.Map(mapDiv, { 
		zoom: 5,
		center: new google.maps.LatLng(37.7718079,-122.3980182)
	});
      var labels = 'Our office';
      // var labelIndex = 0;

	var smallIcon = {
		url: "static/icon.jpg", // url
		scaledSize: new google.maps.Size(50, 50), // scaled size
	}

	newMarker = new google.maps.Marker({
		position: {lat: 37.7718079, lng: -122.3980182},
		map: map,
		icon: smallIcon,
		label: labels,
		draggable: true,
		animation: google.maps.Animation.DROP,
	});


	newMarker.addListener('click', toggleBounce);
	newMarker.setAnimation(google.maps.Animation.BOUNCE);


	google.maps.event.addDomListener(window, "resize", function() {
		var center = map.getCenter();
		google.maps.event.trigger(map, "resize");
		map.setCenter(center);
	});
}

function toggleBounce() {
	if (newMarker.getAnimation() !== null) {
		newMarker.setAnimation(null);
	} else {
		newMarker.setAnimation(google.maps.Animation.BOUNCE);
	}
}
