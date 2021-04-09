<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Andrea Dorigo
  Creation Date: 2021-03-28
  Summary: the file containes the necessary code to be able to implements the heat map.
  Last change date: 2021-03-31
-->

<template>
  <div class="trendGraph">
    <button
    @click="getNumPeopleToday()">STAMPA IL GRAFICO</button>
    <trend
      :data="data"
      :gradient="['#6fa8dc', '#42b983', '#2c3e50']"
      auto-draw
      smooth
    >
    </trend>
  </div>
</template>

<script>

import Elements from '../services/htpprequest';

export default {
  name: 'trendGraph',
  data() {
    return {
      data: []
    }
  },
  methods: {
   getNumPeopleToday: function() {
     console.log("bruh");
     this.data = Elements.getDataRT("Roma","2021-04-3T10").then(data => {
         this.numPeopleToday=data.data;
         console.log("here bruh");
         console.log(this.numPeopleToday);
         return this.numPeopleToday;
      });
    // return this.numPeople;
    this.data = [0,1,2,3,4,5,6];
     return this.data;
    }
  },
  created() {
    // getNumPeopleToday();

  }
}

</script>

<style scoped>
.trendGraph {
  width: 40%;
  margin: 4em auto 0 auto;
}
</style>
