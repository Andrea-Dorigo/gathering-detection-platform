<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: heatMap.vue
  Author: Andrea Dorigo
  Creation Date: 2021-03-28
  Summary: the file containes the code related to the implementation of the heat map.
  Last change date: 2021-05-12
-->

<template>
  <div id="basic-example">
    <div id="myModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <p>Non sono presenti dati per la data o l'ora selezionati</p>
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="closeModal"
        >
          OK
        </button>
      </div>
    </div>
    <l-map
      :zoom="zoom"
      :center="center"
      @update:center="centerUpdated"
      @update:zoom="zoomUpdated"
      :max-zoom="18"
      :min-zoom="15"
    >
      <l-tile-layer
        url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"
      ></l-tile-layer>
      <Vue2LeafletHeatmap
        :lat-lng="latlngs"
        :radius="60"
        :min-opacity="0.75"
        :blur="60"
      ></Vue2LeafletHeatmap>
      <l-marker v-if="zoom > 16" :lat-lng="markerLatLng" :visible="visibility">
        <l-popup id="popup">{{ message }}</l-popup>
      </l-marker>
    </l-map>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from "vue2-leaflet";
import Elements from "../services/htpprequest";
import Vue2LeafletHeatmap from "./Vue2LeafletHeatmap";

export default {
  name: "basicExample",
  components: {
    LMap,
    LTileLayer,
    Vue2LeafletHeatmap,
    LMarker,
    LPopup,
  },
  data() {
    var message = "";
    return {
      latlngs: [[41.899139, 12.473311]],
      center: [41.899139, 12.473311],
      zoom: 15.5,
      markerLatLng: [41.899139, 12.473311],
      message,
      visibility: true,
    };
  },
  methods: {
    retrieveCoordinate: function(date) {
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      var modal = document.getElementById("myModal");
      Elements.getLastValue(city).then((res) => {
        var temp = res.data.time;
        if (new Date(date + ":00:00") <= new Date(temp.replace(" CEST", ""))) {
          var numPeople = 0;
          Elements.getDataRT(city, date).then((res1) => {
            if (res1.data != 0) {
              this.visibility = true;
              numPeople = res1.data[0].numPeople;
              this.markerLatLng = [
                res1.data[0].latitude,
                res1.data[0].longitude,
              ];
              this.message =
                "In " +
                res1.data[0].location +
                " ci sono " +
                numPeople +
                " persone";
              if (res1.data[0].type === 1) {
                this.message = this.message + " [Dati predetti]";
              }
              if (res1.data[0].type === 0) {
                this.message = this.message + " [Dati reali]";
              }
              this.latlngs = [res1.data[0].latitude, res1.data[0].longitude];
              var geoPoints = this.generateRandomPoints(
                { lat: this.latlngs[0], lng: this.latlngs[1] },
                1,
                numPeople
              );
              this.$root.$refs.LHeatmap_component.setHeatLayer(geoPoints);
              this.setCenter(this.latlngs);
            } else {
              modal.style.display = "block";
              this.visibility = false;
              this.$root.$refs.LHeatmap_component.RemoveAll();
              this.message = "Non ci sono dati disponibili";
            }
          });
        } else {
          modal.style.display = "block";
          this.visibility = false;
          this.$root.$refs.LHeatmap_component.RemoveAll();
          this.message = "Non ci sono dati disponibili";
        }
      });
    },
    closeModal: function() {
      var modal = document.getElementById("myModal");
      modal.style.display = "none";
    },
    setCenter: function(value) {
      this.center = value;
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
    generateRandomPoint: function(center, radius) {
      var x0 = center.lng;
      var y0 = center.lat;

      var rd = radius / 111300;

      var u = Math.random();
      var v = Math.random();

      var w = rd * Math.sqrt(u);
      var t = 2 * Math.PI * v;
      var x = w * Math.cos(t);
      var y = w * Math.sin(t);

      var xp = x / Math.cos(y0);

      return { lat: y + y0, lng: xp + x0 };
    },
    generateRandomPoints: function(center, radius, count) {
      var points = [];
      for (var i = 0; i < count; i++) {
        points.push(this.generateRandomPoint(center, radius));
      }
      return points;
    },
    refreshMap: function() {
      var datePicker = this.$root.$refs.datePicker_component.getDate();
      var dateNow = new Date().toISOString().substr(0, 10);
      var timeNow = new Date(Date.now()).getHours().toString();
      if (timeNow.length == 1) timeNow = "0" + timeNow;
      dateNow = dateNow + "T" + timeNow;
      if (datePicker === dateNow) {
        this.retrieveCoordinate(dateNow);
        setInterval(() => this.refreshMap(), 600000);
      }
    },
  },
  created() {
    this.$root.$refs.basicExample_component = this;
    this.$nextTick(this.refreshMap());
  },
};
</script>

<style>
#basic-example {
  width: 80%;
  height: 500px;
}
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}
.modal {
  display: none; /* Hidden by default */
  position: fixed;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
}
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.leaflet-popup-content-wrapper,
.leaflet-popup-tip {
  background: white;
  box-shadow: 0 3px 14px rgba(0, 0, 0, 0.4);
}
</style>
