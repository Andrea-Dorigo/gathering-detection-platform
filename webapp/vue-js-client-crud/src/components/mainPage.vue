<template>

<div id="things">
  <h1>GDP: Gathering Detection Platform</h1>

  <slider/>
  <input type="button" id="reload" value="Reload Map" onClick="reload()"/>
  <div id="map" onload="loadEmptyMap()"></div>
  <div id="calendar">
  <Datepicker :inline="true" v-on:selected="pick" />
	</div>
</div>

</template>

<script>

import slider from './slider.vue'
import Datepicker from 'vuejs-datepicker';


export default {
  name: 'things',
   components: {
    Datepicker,
    slider,
  },
  methods: {
    pick: function(){
      window.alert("ciaone"); 
    }
  }
  }
 
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
