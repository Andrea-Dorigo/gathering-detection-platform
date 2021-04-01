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
        </l-map>
    </div>
</template>

<script>
import { LMap, LTileLayer } from "vue2-leaflet";
import Vue2LeafletHeatmap from './Vue2LeafletHeatmap.vue';
import Elements from '../services/htpprequest';

export default {
  name: 'basicExample',
  components: {
    LMap,
    LTileLayer,
    Vue2LeafletHeatmap
  },
  data() {
    return {
      latlngs: [[41.899139, 12.473311]],
      center: [41.899139, 12.473311],
      zoom: 15,
    };
  },
  methods: {
    retrieveCoordinate : function() {
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      Elements.getCoo(city).then(res => {
          this.latlngs=res.data;
          this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
          this.setCenter(res.data[0]);
          this.$root.$refs.slider_component.setCurTime();
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
