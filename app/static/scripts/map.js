// map.js
$(function($) {
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?sensor=false&callback=initialize";
  document.body.appendChild(script);
});

function initialize() {
  var map;
  var bounds = new google.maps.LatLngBounds();
  var mapOptions = {
    mapTypeId: 'roadmap'
  };

  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  map.setTilt(45);

  var markers = window.markers;

  var marker, position, infoWindowContent = [], infoWindow = new google.maps.InfoWindow();
  for (var i = 0; i < markers.length; i++) {
    position = new google.maps.LatLng(markers[i]['lat'], markers[i]['lng']);
    bounds.extend(position);
    marker = new google.maps.Marker({
      position: position,
      map: map,
      title: markers[i]['title']
    });
    infoWindowContent.push(['<h3>' + markers[i]['title'] + '</h3>']);

    // Allow each marker to have an info window
    google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
            infoWindow.setContent(infoWindowContent[i][0]);
            infoWindow.open(map, marker);
        }
    })(marker, i));

    map.fitBounds(bounds);
  }

  var boundsListener = google.maps.event.addListener((map), 'bounds_changed', function(event) {
      this.setZoom(2);
      google.maps.event.removeListener(boundsListener);
  });
}
