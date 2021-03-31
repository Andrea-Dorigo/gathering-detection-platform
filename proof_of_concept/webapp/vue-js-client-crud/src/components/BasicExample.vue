<template>
    <div class="basic-example">
        <l-map :zoom="10" :center="center" >
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <Vue2LeafletHeatmap   :lat-lng="latlngs" :radius="60" :min-opacity=".75" :max-zoom="18" :min-zoom="16" :blur="60"></Vue2LeafletHeatmap>
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
    };
  },
  methods: {
    retrieveCoordinate : function() {
      var city = this.$root.$refs.autocompleteSearch_component.getNameCity();
      Elements.getCoo(city).then(res => {
          this.latlngs=res.data;
          this.setCenter(res.data[0]);
          this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
          console.log(res.data[0]);
        })
      },
    setCenter: function(value) {
        console.log("entro nel centro")
        console.log(value);
        this.center= value;
      }
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
