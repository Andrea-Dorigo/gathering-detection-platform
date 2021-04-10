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
    <Datepicker id="calendar" :inline="true" v-model="picker" v-on:selected="setDate" format="yyyy-MM-dd"/>
  </div>
  <trendGraph />

	</div>

</template>

<script>

import Datepicker from 'vuejs-datepicker'
import BasicExample from "./BasicExample.vue";
import slider2 from './slider2.vue'
import listCity from './listCity.vue'
import trendGraph from "./trendGraph.vue"


export default {
  name: 'things',
   components: {
    Datepicker,
    BasicExample,
    slider2,
    listCity,
    trendGraph
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
    //Quando si preme ReloadMap
    getRetrieveCoordinate: function(){
      var date = this.picker = new Date().toISOString().substr(0, 10);
      var time = this.$root.$refs.slider2_component.reloadMap();
      date = date + 'T' + time;
      this.$root.$refs.slider2_component.reloadMap();
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    //Quando si seleziona data
    setDate: function(date){
      var d = this.picker = date.toISOString().substr(0, 10);
      // getActualTime ritorna l'ora precisa di adesso, andrà usata getCurTime, non appena capisco come aggiungere sec e ms
      var t = this.$root.$refs.slider2_component.getTime();
      console.log(t)
      d = d + 'T' + t;
      this.$root.$refs.basicExample_component.retrieveCoordinate(d);
    },
    getDate: function() {
      return this.picker;
    },

  }

}
</script>

<style scope>
#things {
   z-index: -2;
}
#slider{
  z-index: 0;
  margin-left: 30px;
  margin-right: 20px;
  width: 90%;
}
#sb {
  z-index: -1;
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
  z-index: 0;
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
