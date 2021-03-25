<template>

<div id="things">
  <slider/>
  <button type="button" value="Reload Map" @click="ricarica">Reload map</button>
  <div id="mc">
  <div id="map"></div>
  <div id="calendar">
    <Datepicker :inline="true" v-on:selected="pick" />
  </div>
  </div>
	</div>
  
</template>

<script>

import $ from 'jquery'
import slider from './slider.vue'
import Datepicker from 'vuejs-datepicker'
import L from 'leaflet'
import Elements from '../services/htpprequest'
import 'leaflet-svg-shape-markers'
import {heatLayer} from 'leaflet'

var map;

export default {
  name: 'things',
   components: {
    Datepicker,
    slider
  },
  data() {
    var coords= [];
    return {
      coords,
    }
  },
  methods: {
    GetHeatLayer: function() {
      heatLayer();
    },
    retrieveCoordinate : function() {
      console.log("sono nel retrieve");
      Elements.getCoordinate().then(res => {
        console.log(res.data);
        this.coords=res.data;
        console.log(this.coords);
        this.loadMap(this.coords);
      })
    },
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
    },
    loadMap: function(data){
      map = L.map('map').setView([41.9005213979, 12.4765647604], 12);
      var tiles = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      })

      tiles.addTo(map);
      
      console.log("ciaone andrea cecchin");

      console.log(data);

      var dataToString = JSON.stringify(data);
      
      var datatext = '{"webcam":' + dataToString + '}';
      
      var test = JSON.parse(datatext);

      console.log(test);
      
      var count = Object.keys(test.webcam).length;
      var last = count-1;
        
      var randomGeoPointsPiazzaNavona = this.generateRandomPoints({'lat':test.webcam[last].latitude, 'lng':test.webcam[last].longitude}, 10, test.webcam[last].numPeople); //piazza navona

      var heat = L.GetHeatLayer(randomGeoPointsPiazzaNavona);

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
    this.loadMap(Elements.getCoordinate());
    },
    ricarica: function() {
      this.$el="map";
      map.remove();
      this.retrieveCoordinate();
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
  }
  },
    mounted() {
        this.$el="map";
        this.loadEmptyMap();
    }
  }
 
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scope>
#map {
  position: absolute;
  width: 800px;
  height: 600px;
  float: right;
}
#calendar{
  position: relative;
  float: right;
}
#mc{
  width: 1400px;
  position: relative;
}
</style>
