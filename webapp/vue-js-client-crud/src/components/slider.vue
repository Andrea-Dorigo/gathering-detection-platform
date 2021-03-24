<template>
    <div id="slider">
    <input @change="setColor()" v-model="value" type="range" id="myRange" class="mySlider" min="0" max="24" onchange="getTime()"/>
    <span :style="setColor()" class="rangeValue" id="range"> {{ value }} </span>
    </div>
</template>

<script>
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
        }
    },
});
</script>
