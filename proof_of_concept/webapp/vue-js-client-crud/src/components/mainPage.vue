<template>

<div id="things">
  <div id="sb">
  <slider/>
  <!-- <LHeatmap/> -->
  <BasicExample />
  <button type="button" value="Reload Map">Reload map</button>
  </div>
  <div id="mc">
  <!-- <GoogleMap /> -->
  <div id="calendar">
   <Datepicker :inline="true" />
  </div>
  </div>
	</div>

</template>

<script>

import slider from './slider.vue'
import Datepicker from 'vuejs-datepicker'
import Elements from '../services/htpprequest'
import BasicExample from "./BasicExample.vue";

// import GoogleMap from './googleMap.vue'

// import LHeatmap from './Vue2LeafletHeatmap.vue'

export default {
  name: 'things',
   components: {
    Datepicker,
    slider,
    BasicExample
    // LHeatmap
  },
  data() {
    var coords= [];
    return {
      coords,
    }
  },
  methods: {
    retrieveCoordinate : function() {
      console.log("sono nel retrieve");
      Elements.getCoordinate().then(res => {
        console.log(res.data);
        this.coords=res.data;
        console.log(this.coords);
        this.loadMap(this.coords);
      })
    },
    mounted() {
        this.$el="map";
        this.loadMap();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scope>
#sb {
  display: inline;
}
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
