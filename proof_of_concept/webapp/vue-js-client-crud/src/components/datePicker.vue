<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: datePicker.vue
  Author: Margherita Mitillo
  Creation Date: 2021-04-12
  Summary: the file containes the code related to the date-picker.
  Last change date: 2021-04-30
-->

<template>
  <div id="calendar">
    <Datepicker
      :inline="true"
      v-model="picker"
      v-on:selected="setDate"
      format="yyyy-MM-dd"
    />
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker";

export default {
  name: "datePicker",
  components: {
    Datepicker,
  },
  data() {
    var picker = new Date().toISOString().substr(0, 10);
    return {
      picker,
    };
  },
  methods: {
    setDate: function(date) {
      var d = (this.picker = date.toISOString().substr(0, 10));
      var t = this.$root.$refs.slider_component.getTime();
      d = d + "T" + t;
      this.$root.$refs.basicExample_component.retrieveCoordinate(d);
    },
    getDate: function() {
      var date = this.picker;
      if (typeof date !== "string") {
        date = date.toISOString().substr(0, 10);
      }
      var t = this.$root.$refs.slider_component.getTime();
      date = date + "T" + t;
      return date;
    },
    resetDate: function() {
      this.picker = new Date(Date.now()).toISOString().substr(0, 10);
    },
  },
  created() {
    this.$root.$refs.datePicker_component = this;
  },
};
</script>

<style scoped>
#calendar {
  /* z-index: 0;
  padding-right: 20px;
  padding-top: 150px;
  margin-left: 50px; */
  padding: 0.5em;
  margin: 0.5em;
}


/**/
.vdp-datePicker_calendar {
  width: 100%;
  height: 100%;
  min-width: 280px;
}
</style>
