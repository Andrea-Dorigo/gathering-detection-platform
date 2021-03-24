<template>

<div id="things">
  <h1>GDP: Gathering Detection Platform</h1>
  <slider/>
  <button type="button" value="Reload Map" @click="reload()">Reload map</button>
  <div id="calendar"></div>
  <Datepicker :inline="true" v-on:selected="pick" />
  <div id="map"></div>
	</div>
  
</template>

<script>

import slider from './slider.vue'
import Datepicker from 'vuejs-datepicker';
import L from 'leaflet'
var map;

export default {
  name: 'things',
   components: {
    Datepicker,
    slider
  },
  methods: {
    pick: function(){
      window.alert("ciaone"); 
    },
    loadEmptyMap: function(){
      this.$el="map";
      console.log("crea mappa vuota");
      map = L.map('map').setView([41.9005213979, 12.4765647604], 12);
      console.log("metti la mappa vuota");
      var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    });
    tiles.addTo(map);
    }
    },
    loadMap: function(data){
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
      
    var randomGeoPointsPiazzaNavona = this.generateRandomPoints({'lat':test.webcam[last].latitude, 'lng':test.webcam[last].longitude}, 10, test.webcam[last].numPeople); //piazza navona

    var heat = L.heatLayer(randomGeoPointsPiazzaNavona);

    heat.addTo(map);

    var marker = L.marker([test.webcam[last].latitude , test.webcam[last].longitude], {
      elevation: 260.0,
      title: "Piazza Navona"
    }).addTo(map);

    marker.bindPopup("Piazza Navona: " + test.webcam[last].numPeople + " persone ca.").openPopup();
    
    var t = test.webcam[last].time;
    t = t.split(".");
    document.getElementById("myRange").value = t[0];
    document.getElementById("range").textContent = t[0];
  },
    generateRandomPointCR: function(center, radius) {
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
    },
    generateRandomPoints: function(center, radius, count) {
    var points = [];
    for (var i=0; i<count; i++) {
    points.push(this.generateRandomPointCR(center, radius));
    }
    return points;
    },
    start: function() {
    var methodurl = "/coordinate";
    // eslint-disable-next-line no-undef
    $.ajax({
    type: 'GET',
    url: methodurl,
    dataType: 'json', 
    success: function(data) {
    this.loadMap(data);
    }
	});
    },
    reload: function() {
    map.remove();
    this.start();
    },
    loadMapByTime: function(dataFinal, index){
      
      map = L.map('map').setView([41.9005213979, 12.4765647604], 12);

      var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      });
      tiles.addTo(map);
      var randomGeoPointsPiazzaNavona = this.generateRandomPoints({'lat':dataFinal.webcam[index].latitude, 'lng':dataFinal.webcam[index].longitude}, 10, dataFinal.webcam[index].numPeople); //piazza navona

      var heat = L.heatLayer(randomGeoPointsPiazzaNavona);
      heat.addTo(map);
      var marker = L.marker([dataFinal.webcam[index].latitude , dataFinal.webcam[index].longitude], {
              elevation: 260.0,
              title: "Piazza Navona"
      }).addTo(map);

      marker.bindPopup("Piazza Navona: " + dataFinal.webcam[index].numPeople + " persone ca.").openPopup();
    },
    getTime: function(){
	
    var methodurl = "/coordinate";
    // eslint-disable-next-line no-undef
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
            this.loadEmptyMap();
          }
          else{
            var r = test.webcam[i].time;
            r = r.split(".");
            document.getElementById("myRange").value = r[0];
            document.getElementById("range").textContent = r[0];
            this.loadMapByTime(test,i);
          }
        }
    });
  },
    mounted:function() {
        this.$el="map";
        console.log("ahahah");
        this.loadEmptyMap();
    }
  }
 
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scope>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
#map {
  position: absolute;
  width: 800px;
  height: 600px;
  float: right;
}
</style>
