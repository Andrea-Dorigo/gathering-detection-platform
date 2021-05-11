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
      <div>
        <date-picker />
        <button
          id="scaricaDati"
          type="button"
          class="btn btn-outline-primary"
          value="Scarica i dati in formato pdf"
          @click="exportpdf"
        >
          Scarica i dati
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

export default {
  name: "mainPage",
  components: {
    datePicker,
    heatMap,
    slider,
    listCity
  },
  methods: {
    //Quando si preme ReloadMap
    getRetrieveCoordinate: function() {
      this.$root.$refs.datePicker_component.resetDate();
      this.$root.$refs.slider_component.reloadMap();
      var date = this.$root.$refs.datePicker_component.getDate();
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    exportpdf: function() {
      var doc = new jsPDF();
      var text = new Array();
      text[0] = "Dati della città di "+this.$root.$refs.autocompleteSearch_component.getNameCity();
      text[1] = ""
      Elements.getDataRT(this.$root.$refs.autocompleteSearch_component.getNameCity(),this.$root.$refs.datePicker_component.getDate()).then((res) => {
      if(res.data!=0){
      text[2] = "Id webcam: "+res.data[0].id_webcam;
      console.log(res.data[0].id_webcam);
      text[3]="Latitudine: "+res.data[0].latitude;
      text[4]="Longitudine: "+res.data[0].longitude;
      text[5]="Numero di persone: "+res.data[0].numPeople;
      text[6]="Data e ora: "+res.data[0].date;
      if(res.data[0].type==0) text[7]="Tipologia di dati: Reali";
      else text[7]="Tipologia di dati: Predetti";
      text[8]="Meteo: "+res.data[0].weather_description;
      text[9]="Temperatura: "+res.data[0].temperature;
      text[10]="Giorno della settimana: "+res.data[0].day_of_week;
      doc.text(text, 10, 10);
      doc.save("dati.pdf");
      } else {
        window.alert("rdrr");
      }
      });
    },
  },
  created() {
    this.$root.$refs.mainPage_component = this;
  },
};
</script>

<style scope>
#scaricaDati {
  margin: 5% 0% 2% 40%;
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
