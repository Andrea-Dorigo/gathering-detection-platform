<template>
  <div>
    <div id="myModalC" class="modalC">
      <div class="modal-contentC">
        <span class="closeC" @click="closeModalC">&times;</span>
        <p>Non sono state inserite entrambe le città oppure non sono presenti dati per la data o l'ora selezionati</p>
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="closeModalC"
        >
          OK
        </button>
      </div>
    </div>
    <div id="ds">
      <date-picker id="datepicker" />
      <div id="sliderCity">
        <div id="sb">
          <slider id="slider" />
          <button
            @click="refreshAll"
            type="button"
            class="btn btn-outline-primary"
            value="Ricarica dati"
          >
            Ricarica dati
          </button>
        </div>
        <div>
          <button
            @click="changeFirstCity"
            id="firstButton"
            type="button"
            class="btn btn-outline-primary"
            value="Scegli la città"
          >
            Scegli la prima città
            <div
              :key="item"
              v-for="(item, index) in suggestiondata1"
              @click="itemSelection1(index)"
            >
              {{ item }}
            </div>
          </button>
          <button
            @click="changeSecondCity"
            id="secondButton"
            type="button"
            class="btn btn-outline-primary"
            value="Scegli la città"
          >
            Scegli la seconda città
            <div
              :key="item"
              v-for="(item, index) in suggestiondata2"
              @click="itemSelection2(index)"
            >
              {{ item }}
            </div>
          </button>
        </div>
        <p>La prima città è: {{ itemSelected1 }}</p>
        <p>La seconda città è: {{ itemSelected2 }}</p>
        <button
          @click="startComparison"
          type="button"
          class="btn btn-outline-primary"
          value="Ricarica dati"
        >
          Confronto
        </button>
        <p id="confrontoResult">
          Nella città di {{ citiy1conf }} ci sono {{ people1conf }} persone
          mentre nella città di {{ citiy2conf }} ci sono
          {{ people2conf }} persone
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import slider from "./slider.vue";
import datePicker from "./datePicker.vue";
import Elements from "../services/htpprequest";

export default {
  name: "confrontoCittà",
  components: {
    slider,
    datePicker,
  },
  data() {
    var suggestiondata1 = [];
    var suggestiondata2 = [];
    var city1 = "";
    var itemSelected1 = "";
    var itemSelected2 = "";
    var datePicked = "";
    var citiy1conf = "";
    var people1conf = "";
    var citiy2conf = "";
    var people2conf = "";
    return {
      suggestiondata1,
      suggestiondata2,
      city1,
      itemSelected1,
      itemSelected2,
      datePicked,
      citiy1conf,
      people1conf,
      citiy2conf,
      people2conf,
    };
  },
  methods: {
    changeFirstCity: function() {
      Elements.getCities().then((res) => {
        if (this.suggestiondata1.length === 0) {
          var place;
          this.suggestiondata1 = [];
          this.cit = res.data;
          place = this.cit;
          this.suggestiondata1 = place;
        } else {
          this.suggestiondata1 = [];
        }
      });
    },
    changeSecondCity: function() {
      Elements.getCities().then((res) => {
        if (this.suggestiondata2.length === 0) {
          var place;
          this.suggestiondata2 = [];
          this.cit = res.data;
          place = this.cit;
          this.suggestiondata2 = place;
        } else {
          this.suggestiondata2 = [];
        }
      });
    },
    itemSelection1: function(index) {
      this.city1 = this.suggestiondata1[index];
      this.itemSelected1 = this.city1;
    },
    itemSelection2: function(index) {
      this.city1 = this.suggestiondata2[index];
      this.itemSelected2 = this.city1;
    },
    startComparison: function() {
      this.datePicked = this.$root.$refs.datePicker_component.getDate();
      this.citiy1conf = this.itemSelected1;
      this.citiy2conf = this.itemSelected2;
      var modal = document.getElementById("myModalC");
      if (this.itemSelected1 !== "" && this.itemSelected2 !== "") {
        Elements.getDataRT(this.itemSelected1, this.datePicked).then((res) => {
          this.people1conf = res.data[0].numPeople;
        });
        Elements.getDataRT(this.itemSelected2, this.datePicked).then((res) => {
          this.people2conf = res.data[0].numPeople;
          var confScritta = document.getElementById("confrontoResult");
          confScritta.style.display = "block";
          modal.style.display = "block";
        });
      } else {
        modal.style.display = "block";
      }
    },
    refreshAll: function() {
      var confScritta = document.getElementById("confrontoResult");
      confScritta.style.display = "none";
      this.suggestiondata1 = [];
      this.suggestiondata2 = [];
      this.city1 = "";
      this.itemSelected1 = "";
      this.itemSelected2 = "";
      this.datePicked = "";
      this.citiy1conf = "";
      this.people1conf = "";
      this.citiy2conf = "";
      this.people2conf = "";
      this.$root.$refs.datePicker_component.resetDate();
      this.$root.$refs.slider_component.reloadMap();
    },
    closeModalC: function() {
      var modal = document.getElementById("myModalC");
      modal.style.display = "none";
    },
  },
  created() {
    this.$root.$refs.confrontoCittà_component = this;
  },
};
</script>

<style>
#slider {
  z-index: 0;
  margin-left: 30px;
  margin-right: 20px;
  width: 80%;
}

#datepicker {
  z-index: 0;
  padding-right: 12px;
  padding-top: 150px;
  margin-left: 50px;
  width: 22%;
}

#sb {
  display: flex;
  width: 95%;
  padding-top: 10px;
  padding-bottom: 10px;
}

#sliderCity {
  width: 75%;
}

#ds {
  display: flex;
}

#firstButton {
  margin: 2% 2% 2% 2%;
}

#secondButton {
  margin: 2% 2% 2% 2%;
}

#confrontoResult {
  display: none;
}

.modal-contentC {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}
.modalC {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  padding-top: 100px; /* Location of the box */
  z-index: 99;
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0, 0, 0); /* Fallback color */
  background-color: rgba(0, 0, 0, 0.4); /* Black w/ opacity */
}
.closeC {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.closeC:hover,
.closeC:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>
