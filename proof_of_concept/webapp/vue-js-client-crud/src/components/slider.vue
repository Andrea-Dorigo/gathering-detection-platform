<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: slider.vue
  Author: Margherita Mitillo
  Creation Date: 2021-04-12
  Summary: the file containes the code related to the slider.
  Last change date: 2021-05-10
-->

<template>
  <div>
    <VueSlideBar
      v-model="slider.value"
      :data="slider.data"
      :range="slider.range"
      :labelStyles="{ color: '#4a4a4a', backgroundColor: '#4a4a4a' }"
      :processStyle="{ backgroundColor: '#d8d8d8' }"
      @callbackRange="callbackRange"
    >
    </VueSlideBar>
  </div>
</template>

<script>
import VueSlideBar from "vue-slide-bar";

var globalTimeCheck = true;
var globalCounter = 0;

export default {
  components: {
    VueSlideBar,
  },
  name: "slider",
  data() {
    return {
      rangeValue: {},
      slider: {
        value: parseInt(new Date(Date.now()).getHours().toString(), 10),
        data: [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
        ],
        range: [
          {
            label: "01",
          },
          {
            label: "02",
          },
          {
            label: "03",
          },
          {
            label: "04",
          },
          {
            label: "05",
          },
          {
            label: "06",
          },
          {
            label: "07",
          },
          {
            label: "08",
          },
          {
            label: "09",
          },
          {
            label: "10",
          },
          {
            label: "11",
          },
          {
            label: "12",
          },
          {
            label: "13",
          },
          {
            label: "14",
          },
          {
            label: "15",
          },
          {
            label: "16",
          },
          {
            label: "17",
          },
          {
            label: "18",
          },
          {
            label: "19",
          },
          {
            label: "20",
          },
          {
            label: "21",
          },
          {
            label: "22",
          },
          {
            label: "23",
          },
          {
            label: "24",
          },
        ],
      },
    };
  },
  methods: {
    callbackRange: function(val) {
      if (globalCounter !== 0) {
        globalTimeCheck = false;
      } else {
        globalCounter = globalCounter + 1;
      }
      this.rangeValue = val;
      var date = this.$root.$refs.datePicker_component.getDate();
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    reloadMap: function() {
      var timeString = new Date(Date.now()).getHours().toString();
      var time = parseInt(timeString, 10);
      this.slider.value = time;
      globalTimeCheck = true;
      globalCounter = 0;
      return time;
    },
    getTime: function() {
      return this.rangeValue.label;
    },
    refreshSlider: function() {
      var timeNow = new Date(Date.now()).getHours().toString();
      var timeSlider = this.getTime();
      if (timeSlider.length == 1) timeSlider = "0" + timeSlider;
      var datePicker = this.$root.$refs.datePicker_component.getDate();
      datePicker = datePicker.split("T");
      var dateNow = new Date().toISOString().substr(0, 10);
      if (
        timeNow !== timeSlider &&
        globalTimeCheck === true &&
        datePicker[0] === dateNow
      ) {
        this.reloadMap();
        setInterval(() => this.refreshSlider(), 120000);
      } else {
        setInterval(() => this.refreshSlider(), 120000);
      }
    },
  },
  created() {
    this.rangeValue.label = new Date(Date.now()).getHours().toString();
    if (this.rangeValue.label.length == 1)
      this.rangeValue.label = "0" + this.rangeValue.label;
    this.$root.$refs.slider_component = this;
    this.$nextTick(this.refreshSlider());
  },
};
</script>
