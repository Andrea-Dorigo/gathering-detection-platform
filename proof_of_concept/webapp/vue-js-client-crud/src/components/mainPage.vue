<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file containes the code related to all the components presents in the webapp.
  Last change date: 2021-04-01
-->

<template>

<div id="things">
  <div id="sb">
  <slider/>
   <button type="button" value="Reload Map" @click="getRetrieveCoordinate">Reload map</button>
  </div>
  <div id="mc">
    <BasicExample id="map"/>
    <div id="calendar">
   <Datepicker :inline="true" v-model="picker" @dayclick='dayClicked'/>
  </div>
  </div>
	</div>

</template>

<script>

import slider from './slider.vue'
import Datepicker from 'vuejs-datepicker'
import BasicExample from "./BasicExample.vue";


export default {
  name: 'things',
   components: {
    Datepicker,
    slider,
    BasicExample
  },
  data() {
    var coords= [];
    var picker= new Date().toISOString().substr(0, 10);
    return {
      coords,
      picker,
    }
  },
  methods: {
    getRetrieveCoordinate: function(){
      this.$root.$refs.basicExample_component.retrieveCoordinate();
      this.picker = new Date().toISOString().substr(0, 10);
    },
    /*dayClicked(date){
      
      console.log(date);
      this.picker = date.getTime();
      console.log(this.picker);
    }*/
  },
}
</script>

<style scope>
slider{
  width: 80%;
}
#sb {
  display: flex;
  width: 100%;
  padding-top: 10px;
  padding-bottom:10px;
}
#sb button {
  width: 20%;
  float:right;
}
#map {
  position: absolute;
  width: 1200px;
  height: 600px;
  float: left;
}
#calendar{
  position: relative;
  float: right;
}
#mc{
  display: inline;
  width:100%;
}
</style>
