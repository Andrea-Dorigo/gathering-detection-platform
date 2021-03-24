<script>
/* eslint-disable no-unused-vars */
/* eslint-disable no-mixed-spaces-and-tabs */
/* eslint-disable no-undef */
console.log("ahahah")

var map;

var L;

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
 
  var rd = radius/111300;

  var u = Math.random();
  var v = Math.random();

  var w = rd * Math.sqrt(u);
  var t = 2 * Math.PI * v;
  var x = w * Math.cos(t);
  var y = w * Math.sin(t);

  var xp = x/Math.cos(y0);

  return {'lat': y+y0, 'lng': xp+x0};
}

function loadMap(data){
	map = L.map('map').setView([41.9005213979, 12.4765647604], 12);

	var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
	})

	tiles.addTo(map);
	
	var dataToString = JSON.stringify(data);
	
	var datatext = '{"webcam":' + dataToString + '}';
	
	var test = JSON.parse(datatext);
	
	var count = Object.keys(test.webcam).length;
    var last = count-1;
    
	var randomGeoPointsPiazzaNavona = generateRandomPoints({'lat':test.webcam[last].latitude, 'lng':test.webcam[last].longitude}, 10, test.webcam[last].numPeople); //piazza navona

	var heat = L.heatLayer(randomGeoPointsPiazzaNavona);

	heat.addTo(map);

	var marker = L.marker([test.webcam[last].latitude , test.webcam[last].longitude], {
		elevation: 260.0,
		title: "Piazza Navona"
	}).addTo(map);

	marker.bindPopup("Piazza Navona: " + test.webcam[last].numPeople + " persone ca.").openPopup();
	
	var t = test.webcam[last].time;
	t = t.split(".");
	myRange.value = t[0];
	range.textContent = t[0];
}


function start() {
	var methodurl = "/coordinate";
	$.ajax({
		type: 'GET',
	    url: methodurl,
	    dataType: 'json', 
	    success: function(data) {
	        loadMap(data);
	    }
	});
}

function reload() {
	map.remove();
	start();
}

function loadEmptyMap(){
	map = L.map('map').setView([41.9005213979, 12.4765647604], 12);

	var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
	});

	tiles.addTo(map);
}

function loadMapByTime(dataFinal, index){
	
	map = L.map('map').setView([41.9005213979, 12.4765647604], 12);

	var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
	}).addTo(map);
	
	var randomGeoPointsPiazzaNavona = generateRandomPoints({'lat':dataFinal.webcam[index].latitude, 'lng':dataFinal.webcam[index].longitude}, 10, dataFinal.webcam[index].numPeople); //piazza navona

	var heat = L.heatLayer(randomGeoPointsPiazzaNavona).addTo(map);

	var marker = L.marker([dataFinal.webcam[index].latitude , dataFinal.webcam[index].longitude], {
	        elevation: 260.0,
	        title: "Piazza Navona"
	}).addTo(map);

	marker.bindPopup("Piazza Navona: " + dataFinal.webcam[index].numPeople + " persone ca.").openPopup();
	

}

function getTime(){
	
	var methodurl = "/coordinate";
	$.ajax({
		type: 'GET',
	    url: methodurl,
	    dataType: 'json', 
	    success: function(data) {
	    	map.remove();
	    	var dataToString = JSON.stringify(data);
	    	var datatext = '{"webcam":' + dataToString + '}';
	    	var test = JSON.parse(datatext);
	    	var t = document.getElementById("myRange").value;
	    	var ore;
	    	var s;
	    	var k = Object.keys(test.webcam).length;
	    	for (var i = 0; i < k; i++){
	    		s = test.webcam[i].time;
	    		ore = s.split(".");
	    		if(ore[0] == t){
	    			break;
	    		}
	    	}
	    	if(i == test.webcam.length){
				document.getElementById("myRange").value = t;
				document.getElementById("range").textContent = t;
	    		alert("Non ci sono dati disponibili per questa fascia oraria");
	    		loadEmptyMap();
	    	}
	    	else{
	    		var r = test.webcam[i].time;
		    	r = r.split(".");
		    	document.getElementById("myRange").value = r[0];
		    	document.getElementById("range").textContent = r[0];
	    		loadMapByTime(test,i);
	    	}
	    }
	});
}


</script>
