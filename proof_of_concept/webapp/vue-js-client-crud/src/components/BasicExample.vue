<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Andrea Dorigo
  Creation Date: 2021-03-28
  Summary: the file containes the code related to implementation of the heat map. 
  Last change date: 2021-03-31
-->

<template>
    <div class="basic-example">
        <l-map :zoom="zoom" :center="center" @update:center="centerUpdated" @update:zoom="zoomUpdated" :max-zoom="18" :min-zoom="15" >
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <Vue2LeafletHeatmap   :lat-lng="latlngs" :radius="60" :min-opacity=".75" :blur="60"></Vue2LeafletHeatmap>
            <l-marker v-if="zoom>16" :lat-lng="markerLatLng">
                <l-popup>{{message}}</l-popup>
            </l-marker>
        </l-map>
    </div>
</template>

<script>

import {LMap, LTileLayer, LMarker, LPopup} from 'vue2-leaflet';
import Vue2LeafletHeatmap from './Vue2LeafletHeatmap.vue';
import Elements from '../services/htpprequest';

export default {
  name: 'basicExample',
  components: {
    LMap,
    LTileLayer,
    Vue2LeafletHeatmap,
    LMarker,
    LPopup
  },
  data() {
    var message='';
    return {
      latlngs: [[41.899139, 12.473311]],
      center: [41.899139, 12.473311],
      zoom: 15,
      markerLatLng: [41.899139, 12.473311],
      message,
    };
  },
  methods: {
    /*retrieveCoordinate : function() {
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      Elements.getCoo(city).then(res => {
          this.latlngs=res.data;
          this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
          this.setCenter(res.data[0]);
          this.$root.$refs.slider_component.setCurTime();
        })
      },*/
    retrieveCoordinate : function(date) {
      var numPeople = 0;
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      console.log("1");
      Elements.getDataRT(city,date).then(res => {
        if( res.data != 0) {
            console.log(res.data)
            numPeople = res.data[0].numPeople;
            this.markerLatLng= [res.data[0].latitude, res.data[0].longitude];
            this.message='In '+ res.data[0].location + ' ci sono '+numPeople+' persone';
            this.latlngs = [res.data[0].latitude, res.data[0].longitude];
            var geoPoints = this.generateRandomPoints({'lat': this.latlngs[0], 'lng':this.latlngs[1]}, 10, numPeople);
            this.$root.$refs.LHeatmap_component.setHeatLayer(geoPoints);
            this.setCenter(this.latlngs);
            console.log(this.latlngs)
        }
        else {
            //rimuovere colore non sono riuscita con removeLayer
            //mettere alert migliore 
            this.message='Non ci sono dati disponibili';
            alert("Non ci sono dati disponibili");
        }  
        })
        /*Elements.getCoo(city).then(res => {
           console.log("3");
                  this.latlngs=res.data[0];
                  var geoPoints = this.generateRandomPoints({'lat': this.latlngs[0], 'lng':this.latlngs[1]}, 10, numPeople);
                  this.$root.$refs.LHeatmap_component.setHeatLayer(geoPoints);
                  this.setCenter(res.data[0]);
              })*/
    },
    setCenter: function(value) {
        this.center= value;
      },
    centerUpdated: function(center) {
      this.center = center;
    },
    zoomUpdated: function(zoom) {
      this.zoom = zoom;
    },
    placePopUp: function(place) {
        this.markerLatLng = place;
    },
    setMessagePopUp: function(numPeople) {
        //bisogna prendere place, per es Piazza Navona
        this.message = "Roma: " + numPeople + " persone ca."
    },
    generateRandomPoint: function(center, radius) {
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
            points.push(this.generateRandomPoint(center, radius));
        }
        return points;
    },
  },
  created() {
    this.$root.$refs.basicExample_component = this;
  }
}
</script>

<style>
.basic-example {
  width: 80%;
  height: 500px;
}
</style>
