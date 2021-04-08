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
      <div>
        <span>Zoom: {{ zoom }}</span>
      </div>
        <l-map :zoom="zoom" :center="center" @update:center="centerUpdated" @update:zoom="zoomUpdated" :max-zoom="18" :min-zoom="15" >
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <Vue2LeafletHeatmap   :lat-lng="latlngs" :radius="60" :min-opacity=".75" :blur="60"></Vue2LeafletHeatmap>
            <l-marker :lat-lng="markerLatLng">
                <l-popup> {{message}}</l-popup>
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
    return {
      latlngs: [[41.899139, 12.473311]],
      center: [41.899139, 12.473311],
      zoom: 15,
      markerLatLng: [41.899139, 12.473311],
      message: ''
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
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      //prende num persone in quella data 
      Elements.getDataRT(city,date).then(res => {
        var numPeople = res.data;
        this.setMessagePopUp(res.data);
          if( res.data != 0) {
             //prende le coordinate della città
              Elements.getCoo(city).then(res => {
                  this.markerLatLng = res.data[0];
                  this.latlngs=res.data;
                  var geoPoints = this.generateRandomPoints({'lat': this.latlngs.latitude, 'lng':this.latlngs.longitude}, 10, numPeople);
                  this.$root.$refs.LHeatmap_component.setHeatLayer(geoPoints);
                  this.setCenter(res.data[0]);
              })
          }
          else {
            //rimuovere colore non sono riuscita con removeLayer
            //mettere alert migliore 
            alert("Non ci sono dati disponibili");
          }  
        })
        
        
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
