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
  <div id="mc">
    <listCity/>
    <div id="sliderMap">
      <div id="sb">
    <slider2 id="slider"/>
    <button type="button" class="btn btn-outline-primary" value="Reload Map" @click="getRetrieveCoordinate">Reload map</button>
    </div>
    <BasicExample id="map"/>
    </div>
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
    listCity,
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
    created() {
    this.$root.$refs.mainPage_component = this;
  }
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
  width: 80%;
}
#sb>button {
  margin-top: 30px;
  margin-left: 60px;
  margin-right: 0px;
  height: 35%;
  width: 15%;
}
#sb {
  z-index: -1;
  display: flex;
  width: 95%;
  padding-top: 10px;
  padding-bottom:10px;
}
#map {
  padding-right: 20px;
  width: 1200px;
  height: 600px;
  margin-left: 20px;
}
#calendar{
  z-index: 0;
  padding-right: 20px;
  padding-top: 150px;
  padding-left: 20px;
  margin-left: 50px;
}
#mc{
  padding-top: 10px;
  display: flex;
  width:100%;
}
</style>
