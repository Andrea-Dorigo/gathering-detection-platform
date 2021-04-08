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
  <slider2 id="slider"/>
   <button type="button" class="btn btn-outline-primary" value="Reload Map" @click="getRetrieveCoordinate">Reload map</button>
  </div>
  <div id="mc">
    <listCity/>
    <BasicExample id="map"/>
    <div id="calendar">
   <Datepicker :inline="true" v-model="picker" v-on:selected="setDate" format="yyyy-MM-dd"/>
  </div>
  </div>
	</div>

</template>

<script>

import Datepicker from 'vuejs-datepicker'
import BasicExample from "./BasicExample.vue";
import slider2 from './slider2.vue'
import listCity from './listCity.vue'


export default {
  name: 'things',
   components: {
    Datepicker,
    BasicExample,
    slider2,
    listCity
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
#things {
   z-index: -11;
}
#slider{
  z-index: -11;
  margin-left: 30px;
  margin-right: 20px;
  width: 90%;
}
#sb {
  z-index: 0;
  display: flex;
  width: 100%;
  padding-top: 10px;
  padding-bottom:10px;
}
#map {
  padding-left: 100px;
  padding-right: 20px;
  width: 1200px;
  height: 600px;
  margin-left: 20px;
}
#calendar{
  z-index: -11;
  padding-right: 20px;
  padding-left: 20px;
  margin-left: 100px;
}
#mc{
  padding-top: 10px;
  display: flex;
  width:100%;
}
</style>
