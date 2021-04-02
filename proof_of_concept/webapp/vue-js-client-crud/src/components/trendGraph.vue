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
    <trend
      :data="[0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0]"
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
  // methods: {
  //  getNumPeopleToday: function() {
  //    Elements.getCoo("Roma").then(res => {
  //        this.latlngs=res.data;
  //        console.log(this.latlngs);
  //     });
  //  },
  created() {
    console.log("bruh");
    Elements.getNumPeopleToday("Roma").then(res => {
        this.numPeopleToday=res.data;
        console.log(this.numPeopleToday);
     });
  }
}

</script>

<style scoped>
.trendGraph {
  width: 40%;
  margin: 4em auto 0 auto;
}
</style>
