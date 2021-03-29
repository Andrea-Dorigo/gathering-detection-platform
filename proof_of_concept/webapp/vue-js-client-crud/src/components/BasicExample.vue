<template>
    <div class="basic-example">
      <button type="button" value="Reload Map" >Reload map</button>
        <l-map style="height: 100%; overflow: auto;" :zoom="10" :center="[47.334852, -1.509485]">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <Vue2LeafletHeatmap :lat-lng="latlngs" :radius="60" :min-opacity=".75" :max-zoom="18" :min-zoom="16" :blur="60"></Vue2LeafletHeatmap>
        </l-map>
    </div>
</template>

<script>
import { LMap, LTileLayer } from "vue2-leaflet";
import Vue2LeafletHeatmap from './Vue2LeafletHeatmap.vue';
import Elements from '../services/htpprequest';

export default {
  components: {
    LMap,
    LTileLayer,
    Vue2LeafletHeatmap
  },
  data() {
    return {
      latlngs: [
        [47.334852, -1.509485, 1],
        [47.342596, -1.328731, 0.75],
        [47.342596, -1.329731, 1],
        [47.342596, -1.329731, 1],
        [47.342596, -1.329731, 1],
        [47.241487, -1.190568, 0.5],
        [47.234787, -1.358337, 1]
      ]
    };
  },
  methods: {
    retrieveCoordinate : function() {
      console.log("sono nel retrieve");
      Elements.getCoordinate().then(res => {
        console.log(res.data);
        this.latlngs=res.data;
        console.log(this.coords);
        this.loadMap(this.coords);
      })
    },
  },
  mounted() {
      this.retrieveCoordinate();
      
  },
 
}
</script>

<style>
.basic-example {
  width: 80%;
  height: 500px;
}
</style>
