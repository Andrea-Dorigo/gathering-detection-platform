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
    <button @click="getNumPeopleToday()">
      Stampa il grafico di oggi (Krk)
    </button>
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
import Elements from "../services/htpprequest";

export default {
  name: "trendGraph",
  data() {
    return {
      data: [],
    };
  },
  methods: {
    getNumPeopleToday: function() {
      var tzoffset = new Date().getTimezoneOffset() * (-1 / 60); //offset in hours (+2, cest)
      var today = new Date();
      today.setHours(0 + tzoffset, 0, 0, 0);
      today = today.toISOString().slice(0, -1);
      this.data = Elements.getNumPeopleToday("Krk", today).then((data) => {
        this.data = data.data;
      });
    },
  },
};
</script>

<style scoped>
.trendGraph {
  width: 60%;
  margin: 4em auto 0 auto;
}
</style>
