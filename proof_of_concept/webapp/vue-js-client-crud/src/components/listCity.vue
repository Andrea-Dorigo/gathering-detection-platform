<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-25
  Summary: the file is the component of the list of the cities.
  Last change date: 2021-03-31
-->

<template>
  <div id="listCity">
    <ul class="list_city">
      <li
        :key="item"
        class="list_city-item"
        v-for="(item, index) in suggestiondata"
        @click="itemSelected(index)"
      >
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
import Elements from "../services/htpprequest";

export default {
  data() {
    var cit = [];
    var searchText = "";
    var suggestiondata = [];
    var name = "Roma";
    return {
      cit,
      searchText,
      suggestiondata,
      name,
    };
  },
  methods: {
    retireveCities: function() {
      Elements.getCities().then((res) => {
        var place;
        this.suggestiondata = [];
        this.cit = res.data;
        place = this.cit;
        this.suggestiondata = place.filter((place) => {
          return place.toLowerCase().includes(this.searchText.toLowerCase());
        });
      });
      //var coo = Elements.getCoo();
    },
    itemSelected: function(index) {
      var date = this.$root.$refs.datePicker_component.getDate();
      this.name = this.suggestiondata[index];
      this.$root.$refs.autocompleteSearch_component.updateCity(this.name);
      Elements.getCoo(this.name).then((res) => {
        this.latlngs = res.data;
        this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
        this.$root.$refs.basicExample_component.setCenter(res.data[0]);
        this.$root.$refs.basicExample_component.placePopUp(res.data[0]);
        this.$root.$refs.basicExample_component.zoomUpdated(15);
        this.$root.$refs.basicExample_component.retrieveCoordinate(date);
      });
    },
    getNameCity: function() {
      return this.name;
    },
    updateCity: function(city) {
      this.name = city;
    },
  },
  created() {
    this.$root.$refs.listCity_component = this;
  },
  mounted() {
    this.retireveCities();
  },
};
</script>

<style scoped>
#listCity ul {
  background-color: white;
  width: 10%;
  position: absolute;
  padding-left: 0px;
}
#listCity ul li {
  border-radius: 2em;
  border: solid 1px black;
  list-style-type: none;
  color: blue;
  padding: 3% 2% 3% 2%;
  margin-bottom: 3%;
}
#listCity ul li:hover {
  cursor: pointer;
}
#listCity {
  padding-left: 20px;
  padding-top: 30px;
}
</style>
