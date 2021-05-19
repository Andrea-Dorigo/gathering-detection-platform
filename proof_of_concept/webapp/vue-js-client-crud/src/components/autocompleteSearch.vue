<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: autocompleteSearch.vue
  Author: Emma Roveroni
  Creation Date: 2021-03-28
  Summary: the file containes the necessary code that implements the search bar for the city, by name and by id.
  Last change date: 2021-05-13
-->

<template>
  <div id="autosearch">
    <div id="mymodalAutocompleteSearch" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <p>La città selezionata non è disponibile</p>
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="closeModal"
        >
          OK
        </button>
      </div>
    </div>
    <div id="noButton">
      <input
        type="text"
        placeholder="Cerca la città.."
        v-model="searchText"
        @keyup="retireveCities"
        @keyup.enter="searchClicked"
        autocomplete="on"
      />
      <div class="suggestion_list" v-if="searchText.length">
        <ul class="list_group">
          <li
            :key="item"
            class="list_group-item"
            v-for="(item, index) in suggestiondata"
            @click="itemSelected(index)"
          >
            {{ item }}
          </li>
        </ul>
      </div>
    </div>
    <button
      class="btn btn-outline-primary"
      type="submit"
      @click="searchClicked"
    >
      Search
    </button>
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
        if (this.searchText != "") {
          this.suggestiondata = place.filter((place) => {
            return place.toLowerCase().includes(this.searchText.toLowerCase());
          });
        }
      });
    },
    itemSelected: function(index) {
      this.name = this.suggestiondata[index];
      this.$root.$refs.listCity_component.updateCity(this.name);
      this.searchText = "";
      this.updateMap(this.name);
    },
    getNameCity: function() {
      return this.name;
    },
    updateCity: function(city) {
      this.name = city;
    },
    searchClicked: function() {
      var modal = document.getElementById("mymodalAutocompleteSearch");
      Elements.getCities().then((res) => {
        Elements.getCityById(this.searchText).then((res1) => {
          console.log(res1.data[0]);
          if (res1.data[0]) {
            this.searchText = res1.data[0];
          }
          var place;
          this.cit = res.data;
          place = this.cit;
          var present = false;
          var i;
          var city;
          for (i = 0; i < place.length; i++) {
            if (this.searchText.toLowerCase() === place[i].toLowerCase()) {
              present = true;
              city = place[i];
            }
          }
          if (present === false) {
            this.searchText = "";
            modal.style.display = "block";
          } else {
            this.name = city;
            this.$root.$refs.listCity_component.updateCity(this.name);
            this.searchText = "";
            this.updateMap(this.name);
          }
        });
      });
    },
    updateMap: function(city) {
      var date = this.$root.$refs.datePicker_component.getDate();
      Elements.getCoo(city).then((res) => {
        this.latlngs = res.data;
        this.$root.$refs.LHeatmap_component.setHeatLayer(this.latlngs);
        this.$root.$refs.basicExample_component.setCenter(res.data[0]);
        this.$root.$refs.basicExample_component.placePopUp(res.data[0]);
        this.$root.$refs.basicExample_component.zoomUpdated(15);
        this.$root.$refs.basicExample_component.retrieveCoordinate(date);
      });
    },
    closeModal: function() {
      var modal = document.getElementById("mymodalAutocompleteSearch");
      modal.style.display = "none";
    },
  },
  created() {
    this.$root.$refs.autocompleteSearch_component = this;
  },
};
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
  background-color: white;
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
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}
.modal {
  display: none; /* Hidden by default */
  position: fixed; 
  padding-top: 100px; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%;
  overflow: auto; 
  background-color: rgb(0, 0, 0); 
  background-color: rgba(0, 0, 0, 0.4); 
}
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>
