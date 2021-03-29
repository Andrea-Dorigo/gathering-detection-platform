<template>
  <div>
      <input type="text" placeholder="Cerca la città.." v-model="searchText" @keyup="retireveCities" autocomplete="on"/>
      <div class="suggestion_list" v-if="searchText.length">
        <ul class="list_group">
          <li :key="item" class="list_group-item" v-for="(item,index) in suggestiondata" @click="itemSelected(index)">{{ item }}</li>
        </ul>
      </div>
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </div>
</template>

<script>
import Elements from '../services/htpprequest'
export default {
  data() {
    var cit= [];
    var searchText='';
    var suggestiondata=[];
    return {
      cit,
      searchText,
      suggestiondata,
    }
  },
    methods:{
      retireveCities : function() {
      Elements.getCities().then(res => {
      var place;
      this.suggestiondata = [];
      this.cit=res.data;
      place=this.cit;
      console.log(this.cit);
      if(this.searchText!='') {
        this.suggestiondata = place.filter(place => {
        return place.toLowerCase().includes(this.searchText.toLowerCase())
      });
      }
      })
      var coo = Elements.getCoo();
      console.log(coo);
    },
      itemSelected: function(index){
        //da completare quando la mappa funziona
         var id = this.suggestiondata[index].id;
         var name = this.suggestiondata[index].name;

         console.log(id);
         console.log(name);

         this.searchText = name;
         this.suggestiondata = [];

      }

    }
}
</script>
