<template>
    <div id="sliderdiv">
    <time-slider  color-main="navy"  color='snow' v-on:current-time="shiftTime($event)" style="width:80%"></time-slider>
    </div>
</template>


<script>
import TimeSlider from 'times-slider'
import {getTime} from "./myfunctions.js"

export default{
  //da completare quando funziona la mappa
  components: {
      TimeSlider
    },
    data: () => ({
        curTime: new Date(Date.now()).toTimeString().slice(0,5)
    }), 
     mounted: function () {
    },
    methods: {
    shiftTime: function(a) {
      this.curTime = a;
    },
    getTimeSlider: function() {
            getTime();
        }
    }
}
</script>

<style scoped>
#sliderdiv{
  width: 80%;
}
</style>