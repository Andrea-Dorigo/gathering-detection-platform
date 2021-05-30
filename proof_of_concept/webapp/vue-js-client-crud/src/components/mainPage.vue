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
    <div class="wrapper">
        <div class="aside aside-1">
          <date-picker />
        </div>
        <div class="topWrapper">
          <div class="subTitle">
            <h2>
              Seleziona l'orario di cui vuoi visualizzare i dati
            </h2>
          </div>
          <slider id="slider" />
          <div class="bottoneRicarica">
            <button
              type="button"
              class="btn btn-outline-primary"
              value="Reload Map"
              @click="getRetrieveCoordinate"
            >
              Ricarica mappa
            </button>
          </div>
        </div>
        <div class="main">
          <heatMap id="map" />
        </div>
        
        <div class="aside aside-2">
          <listCity />
        </div>
        <div class="footer">
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
    </div>
    <!-- <div id="mc">

    </div> -->
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
      var doc = new jsPDF({
        orientation: "p",
        unit: "mm",
        format: 'a4',
        floatPrecision: 16, // or "smart", default is 16
      });
      var text = "";
      text =
        text +
        "Dati della città di \n" +
        this.$root.$refs.autocompleteSearch_component.getNameCity();
      text = text + "\n";
      Elements.getAllValue(
        this.$root.$refs.autocompleteSearch_component.getNameCity()
      ).then((res) => {
        var i;
        for (i = 0; i < res.data.length; i++) {
          text = text + "Latitudine: " + res.data[i].latitude + "\n";
          text = text + "Longitudine: " + res.data[i].longitude + "\n";
          text = text + "Numero di persone: " + res.data[i].numPeople + "\n";
          text = text + "Data e ora: " + res.data[i].date + "\n";
          if (res.data[i].type == 0)
            text = text + "Tipologia di dati: Reali" + "\n";
          text = text + "Tipologia di dati: Predetti" + "\n";
          text = text + "Meteo: " + res.data[i].weather_description + "\n";
          text = text + "Temperatura: " + res.data[i].temperature + "\n";
          text =
            text + "Giorno della settimana: " + res.data[i].day_of_week + "\n";
          text = text + "\n";
        }

        var textWidth=220;
        var lineSpacing= 7;
        var xPosition= 10;
        var initialYPosition= 30;
        var pageWrapInitialYPosition= 10;
        var textLines = doc.splitTextToSize(text, textWidth); // Split the text into lines
        var pageHeight = doc.internal.pageSize.height;        // Get page height, well use this for auto-paging

        var cursorY = initialYPosition;

        textLines.forEach(lineText => {
          if (cursorY > pageHeight) { // Auto-paging
            doc.addPage();
            cursorY = pageWrapInitialYPosition;
          }
          doc.text(xPosition, cursorY, lineText);
          cursorY += lineSpacing;
        })
        var splitTitle = doc.splitTextToSize(text, 180);
        var m;
        for(m=0; m<splitTitle.length; m++) {
          if(splitTitle[m].length>500) doc.addPage();
          doc.text(splitTitle[m],10,10);
        }
        doc.save("dati.pdf");
      });
    },
    exportcsv: function() {
      Elements.getAllValue(
        this.$root.$refs.autocompleteSearch_component.getNameCity()
      ).then((res) => {
        console.log(res.data[0]);
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
        anchor.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
        anchor.target = "_blank";
        anchor.download = "dati.csv";
        anchor.click();
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
  /* z-index: -2; */
}
/* #slider { */
  /* z-index: 0;
  margin-left: 30px;
  margin-right: 20px; */
  /* width: 80%; */

/* #sb > button {
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
} */
#map {
  width: 100%;
  height: 100%;
  min-width: 450px;
  min-height: 240px;
}
/* #mc {
  padding-top: 10px;
  display: flex;
  flex-flow: row wrap;
  text-align: center; */
  /* justify-content: space-around; */
  /* align-content: flex-start; 
} */


/*CSS NUOVO*/

/* #mc > * {
  padding: 10px;
  flex: 1 100%;
}

.header {
  background: tomato;
  margin: auto;
}

.main {
  background: deepskyblue;
  margin: auto;
}
.aside {
  margin: auto;
}

.aside-1 {
   background: gold;
}

.aside-2 {
  background: hotpink;
}

.downloadButtons {
    background: lightgreen;
    margin: auto;
} */

.topWrapper {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  align-items: center;
  margin: 0 3em 0 3em;

  /* background: tomato; */
}

.subTitle {
  margin-top: 1em;
  padding: 0.3em;
}

h2 {
  font-size: 1.5em;
  font-style: italic;
}

 #slider {
   margin: 1em;
   width: 80%;
 }

 .bottoneRicarica {
   float: left;
 }

.wrapper {
  display: flex;
  flex-flow: row wrap;
  font-weight: bold;
  text-align: center;
}

.wrapper > * {
  padding: 10px;
  flex: 1 100%;
}

.header {
  /* background: tomato; */
}

.footer {
  /* align-items: center; */
  /* background: lightgreen; */
}
#scaricaDati {
  margin: 0.5em;
  padding: 0.5em;
}

.main {
  text-align: left;
  /* background: deepskyblue; */
}

.aside-1 {
  align-items: center;
  /* background: gold; */
}

.aside-2 {
  /* background: hotpink; */
}

@media all and (min-width: 500px) {
  .aside { flex: 1 0 0; }
  .topWrapper { order: 1;}
  .main {order: 2; }
  .aside-1{ order: 3;}
  .aside-2 { order: 3;}
  .footer { order: 4;}
  
  /* .main    { flex: 3 0px; }
  .aside-1 { order: 1; }
  .main    { order: 2; }
  .aside-2 { order: 3; }
  .footer  { order: 4; } */

}

@media all and (min-width: 900px) {
  
  .main    { flex: 4; }
  .topWrapper { order: 1;}
  .aside-1 { order: 2; }
  .main    { order: 3; }
  .aside-2 { order: 4; }
  .footer  { order: 5; }

  #listCity ul li {
    /* display: inline; */
    padding: 1% 1% 1% 1% ;
    width: 10%;
    margin-right: 2% ;
  }

}

</style>
