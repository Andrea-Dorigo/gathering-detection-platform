<template>
    <div class="basic-example">
        <l-map style="height: 100%; overflow: auto;" :zoom="10" :center="[47.334852, -1.509485]">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <Vue2LeafletHeatmap :lat-lng="latlngs" :radius="60" :min-opacity=".75" :max-zoom="10" :blur="60"></Vue2LeafletHeatmap>
        </l-map>
    </div>
</template>

<script>
import { LMap, LTileLayer } from "vue2-leaflet";
import Vue2LeafletHeatmap from './Vue2LeafletHeatmap.vue';
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
  }
};
</script>

<style>
.basic-example {
  width: 100%;
  height: 500px;
}
</style>
