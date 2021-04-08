<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: slider.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file containes the code related to the time slider.
  Last change date: 2021-03-31
-->

<template>
    <div id="sliderdiv">
    <time-slider  color-main="navy"  color='snow' v-on:current-time="shiftTime($event)" style="width:80%"></time-slider>
    </div>
</template>


<script>
import TimeSlider from 'times-slider'

export default{
  name: 'slider',
  components: {
      TimeSlider
    },
    data: () => ({
        curTime: new Date(Date.now()).toTimeString().slice(0,5)
    }), 
    methods: {
    shiftTime: function(a) {
      this.curTime = a;
    },
    setActualTime: function() {
      this.curTime =  new Date(Date.now()).toTimeString().slice(0,5);
    },
    //forse si può togliere
    getActualTime: function(){
      var d = new Date(Date.now());
      var s=  d.getSeconds();
      var ms = d.getMilliseconds();
      var time = new Date(Date.now()).toTimeString().slice(0,5) + ':' + s + '.' + ms;
      return time;
    },
    getCurTime: function() {
      return this.curTime;
    }
    },
    created() {
       this.$root.$refs.slider_component = this;
    }
}
</script>

<style scoped>
#sliderdiv{
  width: 80%;
}
</style>