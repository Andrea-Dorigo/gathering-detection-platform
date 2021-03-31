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
    setCurTime: function() {
      console.log(this.curTime);
      console.log("entro?")
      this.curTime =  new Date(Date.now()).toTimeString().slice(0,5);
      console.log(this.curTime);
    },
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