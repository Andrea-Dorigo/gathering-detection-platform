<template>
    <div id="sliderdiv">
    <time-slider id="slider"  color-main="navy"  color='snow' v-on:current-time="shiftTime($event)" v-on:change="getTimeSlider"></time-slider>
    <!--<input @change="setColor()" v-model="value" type="range" id="myRange" class="mySlider" min="0" max="24" v-on:change="getTimeSlider"/>
    <span :style="setColor()" class="rangeValue" id="range"> {{ value }} </span>-->
    </div>
</template>


<script>
import TimeSlider from 'times-slider'
import {getTime} from "./myfunctions.js"

export default{
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
#slider {
    fill: white;
    fill-opacity: 0%;
    width: 80%;
    color: snow;
    stroke: black;
    stroke-width: 2;
    
}
</style>