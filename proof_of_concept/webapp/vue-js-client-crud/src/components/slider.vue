<template>
    <div id="slider">
    <input @change="setColor()" v-model="value" type="range" id="myRange" class="mySlider" min="0" max="24" v-on:change="getTimeSlider"/>
    <span :style="setColor()" class="rangeValue" id="range"> {{ value }} </span>
    </div>
</template>

<script>
 
import {getTime} from "./myfunctions.js";

export default({
    name: 'slider',
    data() {
        return {
            value: ""
        }
    },
    methods: {
        setColor: function() {
            if (this.value > 0) {
                return {
                    color: "#black",
                }

            }
        },
        getTimeSlider: function() {
            getTime;
        }
    },
});
</script>
