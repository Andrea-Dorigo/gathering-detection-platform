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

export default {
  data() {
    return {
      rangeValue: {},
      slider: {
        value: 1,
        data: [
          0,
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
            label: "0",
          },
          {
            label: "1",
          },
          {
            label: "2",
          },
          {
            label: "3",
          },
          {
            label: "4",
          },
          {
            label: "5",
          },
          {
            label: "6",
          },
          {
            label: "7",
          },
          {
            label: "8",
          },
          {
            label: "9",
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
      this.rangeValue = val;
    },
    reloadMap: function() {
      var time = new Date(Date.now()).getHours().toString();
      this.rangeValue = time;
      //manca da spostare visivamente lo slider
      //this.rangeValue.label = time;
      return time;
    },
    getTime: function() {
      //non so come prendere l'orario dopo poichè è una stringa
      return this.rangeValue.label;
    },
  },
  created() {
    this.$root.$refs.slider2_component = this;
  },
  components: {
    VueSlideBar,
  },
};
</script>
