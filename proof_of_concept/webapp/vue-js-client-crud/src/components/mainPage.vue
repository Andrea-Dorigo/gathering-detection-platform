<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file containes the code related to all the components presents in the webapp.
  Last change date: 2021-04-01
-->

<template>
  <div id="mainPage">
    <div id="mc">
      <listCity />
      <div id="sliderMap">
        <div id="sb">
          <slider2 id="slider" />
          <button
            type="button"
            class="btn btn-outline-primary"
            value="Reload Map"
            @click="getRetrieveCoordinate"
          >
            Reload map
          </button>
        </div>
        <BasicExample id="map" />
      </div>
      <date-picker/>
    </div>
  </div>
</template>

<script>
import BasicExample from "./BasicExample.vue";
import slider2 from "./slider2.vue";
import listCity from "./listCity.vue";
import DatePicker from './datePicker.vue';

export default {
  name: "mainPage",
  components: {
    DatePicker,
    BasicExample,
    slider2,
    listCity,
  },
  methods: {
    //Quando si preme ReloadMap o si apre il sito
    getRetrieveCoordinate: function() {
      var date = this.$root.$refs.datePicker_component.getDate();
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    },
    created() {
      this.$root.$refs.mainPage_component = this;
    },
};
</script>

<style scope>
#mainPage {
  z-index: -2;
}
#slider {
  z-index: 0;
  margin-left: 30px;
  margin-right: 20px;
  width: 80%;
}
#sb > button {
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
  padding-bottom: 10px;
}
#map {
  padding-right: 20px;
  width: 1200px;
  height: 600px;
  margin-left: 20px;
}
#mc {
  padding-top: 10px;
  display: flex;
}
</style>
