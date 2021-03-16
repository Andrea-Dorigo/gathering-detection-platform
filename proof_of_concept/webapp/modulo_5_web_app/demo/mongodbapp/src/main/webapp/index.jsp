<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
    <title>Leaflet.heat demo</title>
    <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
    <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
    <script src="leaflet-heat.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<link rel = "stylesheet" href = "style.css" type = "text/css" media = "screen" />
</head>
<body onload="start()">

<h1>GDP: Gathering Detection Platform</h1>
<div id="map"></div>


<script>



function generateRandomPoints(center, radius, count) {
  var points = [];
  for (var i=0; i<count; i++) {
    points.push(generateRandomPoint(center, radius));
  }
  return points;
}


function generateRandomPoint(center, radius) {
  var x0 = center.lng;
  var y0 = center.lat;
  // Convert Radius from meters to degrees.
  var rd = radius/111300;

  var u = Math.random();
  var v = Math.random();

  var w = rd * Math.sqrt(u);
  var t = 2 * Math.PI * v;
  var x = w * Math.cos(t);
  var y = w * Math.sin(t);

  var xp = x/Math.cos(y0);

  // Resulting point.
  return {'lat': y+y0, 'lng': xp+x0};
}

function loadMap(data){
	
	var map = L.map('map').setView([41.9005213979, 12.4765647604], 12);

	var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
	}).addTo(map);
	
	var dataToString = JSON.stringify(data);
	
	var datatext = '{"webcam":' + dataToString + '}';
	
	var test = JSON.parse(datatext);
	
	var count = Object.keys(test.webcam).length;
    var last = count-1;
	
	var randomGeoPointsPiazzaNavona = generateRandomPoints({'lat':test.webcam[last].latitude, 'lng':test.webcam[last].longitude}, 10, test.webcam[last].numPeople); //piazza navona

	var heat = L.heatLayer(randomGeoPointsPiazzaNavona).addTo(map);

	var marker = L.marker([test.webcam[last].latitude , test.webcam[last].longitude], {
	        elevation: 260.0,
	        title: "Piazza Navona"
	}).addTo(map);

	marker.bindPopup("Piazza di Navona: " + test.webcam[last].numPeople + " persone ca.").openPopup();
	
}


function start() {
	var methodurl = "/coordinate";
	$.ajax({
		type: 'GET',
	    url: methodurl,
	    dataType: 'json', 
	    success: function(data) {
	    	console.log(data);
	        loadMap(data);
	    }
	});
}


</script>

</body>
</html>
