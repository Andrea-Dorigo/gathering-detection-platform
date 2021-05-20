<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: mainPage.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file containes the code related to all the components presents in the webapp.
  Last change date: 2021-04-01
-->

<template>
  <div id="mainPage">
    <div id="myModalPDF" class="modalPDF">
      <div class="modal-contentPDF">
        <span class="closePDF" @click="closeModalPDF">&times;</span>
        <p>Non sono presenti dati per la data o l'ora selezionati</p>
        <button
          type="button"
          class="btn btn-outline-primary"
          @click="closeModalPDF"
        >
          OK
        </button>
      </div>
    </div>
    <div id="mc">
      <div>
        <date-picker />
        <button
          id="scaricaDati"
          type="button"
          class="btn btn-outline-primary"
          value="Scarica i dati in formato pdf"
          @click="exportpdf"
        >
          Scarica i dati in formato PDF
        </button>
        <button
          id="scaricaDati"
          type="button"
          class="btn btn-outline-primary"
          value="Scarica i dati in formato pdf"
          @click="exportcsv"
        >
          Scarica i dati in formato CSV
        </button>
      </div>
      <div id="sliderMap">
        <div id="sb">
          <slider id="slider" />
          <button
            type="button"
            class="btn btn-outline-primary"
            value="Reload Map"
            @click="getRetrieveCoordinate"
          >
            Reload map
          </button>
        </div>
        <div id="mapList">
          <heatMap id="map" />
          <listCity />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import heatMap from "./heatMap.vue";
import slider from "./slider.vue";
import listCity from "./listCity.vue";
import datePicker from "./datePicker.vue";
import jsPDF from "jspdf";
import Elements from "../services/htpprequest";
import JsonCSV from "vue-json-csv";
import Vue from "vue";

Vue.component("downloadCsv", JsonCSV);

export default {
  name: "mainPage",
  components: {
    datePicker,
    heatMap,
    slider,
    listCity,
  },
  methods: {
    getRetrieveCoordinate: function() {
      this.$root.$refs.datePicker_component.resetDate();
      this.$root.$refs.slider_component.reloadMap();
      var date = this.$root.$refs.datePicker_component.getDate();
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    exportpdf: function() {
      var modal = document.getElementById("myModalPDF");
      var doc = new jsPDF();
      var text = new Array();
      text[0] =
        "Dati della città di " +
        this.$root.$refs.autocompleteSearch_component.getNameCity();
      text[1] = "";
      Elements.getAllValue(
        this.$root.$refs.autocompleteSearch_component.getNameCity(),
      ).then((res) => {
        if (res.data != 0) {
          var i;
         for (i = 0; i < res.data.length; i++)  {
          text[3] = "Latitudine: " + res.data[i].latitude;
          text[4] = "Longitudine: " + res.data[i].longitude;
          text[5] = "Numero di persone: " + res.data[i].numPeople;
          text[6] = "Data e ora: " + res.data[i].date;
          if (res.data[i].type == 0) text[7] = "Tipologia di dati: Reali";
          else text[7] = "Tipologia di dati: Predetti";
          text[8] = "Meteo: " + res.data[i].weather_description;
          text[9] = "Temperatura: " + res.data[i].temperature;
          text[10] = "Giorno della settimana: " + res.data[i].day_of_week;
          }
          doc.text(text, 10, 10);
          doc.save("dati.pdf");
        } else {
          modal.style.display = "block";
        }
      });
    },
    exportcsv: function() {
      var modal = document.getElementById("myModalPDF");

      Elements.getAllValue(
        this.$root.$refs.autocompleteSearch_component.getNameCity(),
      ).then((res) => {
        console.log(res.data[0])
        if (res.data != 0) {
          var i;
          var dati;
          var csv =
              "Latitudine, Longitudine, Numero di persone, Data e ora, Tipologia di dati, Meteo, Temperatura, Giorno della settimana\n";
          for (i = 0; i < res.data.length; i++) {
            var tipo;
            if (res.data[0].type == 0) tipo = "Tipologia di dati: Reali";
            else tipo = "Tipologia di dati: Predetti";
            dati =
              res.data[i].latitude +
              "," +
              res.data[i].longitude +
              "," +
              res.data[i].numPeople + 
              "," +
              res.data[i].date +
              "," +
              tipo +
              "," +
              res.data[i].weather_description +
              "," +
              res.data[i].temperature +
              "," +
              res.data[i].day_of_week +
              "\n";
            csv = csv + dati;
          }
            const anchor = document.createElement("a");
            anchor.href =
              "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
            anchor.target = "_blank";
            anchor.download = "dati.csv";
            anchor.click();
        } else {
          modal.style.display = "block";
        }
      });
    },
    closeModalPDF: function() {
      var modal = document.getElementById("myModalPDF");
      modal.style.display = "none";
    },
  },
  created() {
    this.$root.$refs.mainPage_component = this;
  },
};
</script>

<style scope>
.modal-contentPDF {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 50%;
}
.modalPDF {
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
.closePDF {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}
.closePDF:hover,
.closePDF:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
#scaricaDati {
  margin: 5% 0% 2% 25%;
  padding: 1% 1% 1% 1%;
}
#mapList {
  display: flex;
}
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
  width: 1200px;
  height: 600px;
}
#mc {
  padding-top: 10px;
  display: flex;
}
</style>
