<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Andrea Dorigo
  Creation Date: 2021-03-28
  Summary: the file containes the necessary code to be able to implements the heat map.
  Last change date: 2021-03-31
-->

<template>
  <div id="autosearch">
    <div id="noButton">
      <input type="text" placeholder="Cerca la città.." v-model="searchText" @keyup="retireveCities" autocomplete="on"/>
      <div class="suggestion_list" v-if="searchText.length">
        <ul class="list_group">
          <li :key="item" class="list_group-item" v-for="(item,index) in suggestiondata" @click="itemSelected(index)">{{ item }}</li>
        </ul>
      </div>
      </div>
      <button class="btn btn-outline-primary" type="submit">Search</button>
    </div>
</template>

<script>

import Elements from '../services/htpprequest'
export default {
  data() {
    var cit= [];
    var searchText='';
    var suggestiondata=[];
    var name='Roma';
    return {
      cit,
      searchText,
      suggestiondata,
      name,
    }
  },
    methods:{
      retireveCities : function() {
      Elements.getCities().then(res => {
      var place;
      this.suggestiondata = [];
      this.cit=res.data;
      place=this.cit;
      if(this.searchText!='') {
        this.suggestiondata = place.filter(place => {
        return place.toLowerCase().includes(this.searchText.toLowerCase())
      });
      }
      })
      //var coo = Elements.getCoo();
    },
    itemSelected: function(index){
      this.name = this.suggestiondata[index];
      Elements.getCoo(this.name).then(res => {
        this.latlngs=res.data;
        this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
        this.$root.$refs.basicExample_component.setCenter(res.data[0]);
      })
    },
    getNameCity : function() {
      return this.name;
    }
  },
  created() {
    this.$root.$refs.autocompleteSearch_component = this;
  }
}
</script>

<style scoped>
.suggestion_list {
  width: 100%;
}
#noButton {
  z-index: 0;
  margin-right: 2%;
  width: 100%;
}
#autosearch {
  width: 30%;
  display: flex;
}
#autosearch input {
  width: 100%;
}
#autosearch ul {
  background-color:white;
  position: absolute;
  z-index: 3;
  width: 426.8px;
  padding-left: 0px;
}
#autosearch ul li {
  padding: 3% 2% 3% 2%;
  border: solid 1px black;
  list-style-type: none;
  color: blue;
}
#autosearch ul li:hover {
  cursor: pointer;
}
</style>