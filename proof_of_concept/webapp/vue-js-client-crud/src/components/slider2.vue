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
  components: {
    VueSlideBar,
  },
  name: "slider2",
  data() {
    return {
      rangeValue: {},
      slider: {
        value: parseInt(new Date(Date.now()).getHours().toString(), 10),
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
            label: "00",
          },
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
      this.rangeValue = val;
      var date = this.$root.$refs.datePicker_component.getDate();
      //if (date.search("Europa"))
      //  date = new Date(date).toISOString().substr(0, 10);
      this.$root.$refs.basicExample_component.retrieveCoordinate(date);
    },
    reloadMap: function() {
      var timeString = new Date(Date.now()).getHours().toString();
      var time = parseInt(timeString, 10);
      this.slider.value = time;
      return time;
    },
    getTime: function() {
      return this.rangeValue.label;
    },
  },
  created() {
    this.$root.$refs.slider2_component = this;
  },
};
</script>
