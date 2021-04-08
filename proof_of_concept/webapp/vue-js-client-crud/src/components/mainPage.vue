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
   <Datepicker :inline="true" v-model="picker" v-on:selected="setDate" format="yyyy-MM-dd"/>
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
      var date = this.picker = new Date().toISOString().substr(0, 10);
      var time = this.$root.$refs.slider_component.getActualTime();
      date = date + 'T' + time + '+00:00'; 
      time = date; 
      var prova = "2021-03-24T09:16:55.110+00:00";
      this.$root.$refs.slider_component.setActualTime();
      this.$root.$refs.basicExample_component.retrieveCoordinate(prova);
    },
    setDate: function(date){
      var d = this.picker = date.toISOString().substr(0, 10);
      // getActualTime ritorna l'ora precisa di adesso, andrà usata getCurTime, non appena capisco come aggiungere sec e ms
      var t = this.$root.$refs.slider_component.getActualTime();
      d = d + 'T' + t + '+00:00'; 
      t = d; 
      var prova = '2021-03-24T12:16:55.234+00:00';
      this.$root.$refs.basicExample_component.retrieveCoordinate(prova);
    },
    getDate: function() {
      return this.picker;
    },

  }

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
