<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: slider2.vue
  Author: Margherita Mitillo
  Creation Date: 2021-04-08
  Summary: the file containes the code related to the time slider.
  Last change date: 2021-04-08
-->

<template>
    <div>
         <vue-slide-bar v-model="sliderWithLabel.value"
                :data="sliderWithLabel.data"
                :range="sliderWithLabel.range"
                :lineHeight="15"
                :labelStyles="{ color: '#4a4a4a', backgroundColor: '#4a4a4a' }"
                :processStyle="{ backgroundColor: '#d8d8d8'}"
                :tooltipStyle="{ translateX: '60.56px'}"
                @callbackRange="callbackRange(sliderWithLabel.value)"
                style="z-index:0">
        </vue-slide-bar>
    </div>
</template>

<script>
import VueSlideBar from 'vue-slide-bar'

  export default {
       components: {
        VueSlideBar
      },
    data () {
              return {
                rangeValue: {},
                sliderWithLabel: {
                value: '13:00',
                data: ['06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00',
                        '17:00','18:00','19:00','20:00','24:00','01:00','02:00','03:00','04:00','05:00'],
                range: [
                  {
                    label: '06:00',
                    isHide: true
                  },
                  {
                    label: '07:00',
                    isHide: true
                  },
                  {
                    label: '08:00',
                    isHide: true
                  },
                  {
                    label: '09:00',
                    isHide: true
                  },
                  {
                    label: '10:00',
                    isHide: true
                  },
                  {
                    label: '11:00',
                    isHide: true
                  },
                  {
                    label: '12:00',
                    isHide: true
                  },
                  {
                    label: '13:00',
                    isHide: true
                  },
                  {
                    label: '14:00',
                    isHide: true
                  },
                  {
                    label: '15:00',
                    isHide: true
                  },
                  {
                    label: '16:00',
                    isHide: true
                  },
                  {
                    label: '17:00',
                    isHide: true
                  },
                  {
                    label: '18:00',
                    isHide: true
                  },
                  {
                    label: '19:00',
                    isHide: true
                  },
                  {
                    label: '20:00',
                    isHide: true
                  },
                  {
                    label: '21:00',
                    isHide: true
                  },
                  {
                    label: '22:00',
                    isHide: true
                  },
                  {
                    label: '23:00',
                    isHide: true
                  },
                  {
                    label: '00:00',
                    isHide: true
                  },
                  {
                    label: '01:00',
                    isHide: true
                  },
                  {
                    label: '02:00',
                    isHide: true
                  },
                  {
                    label: '03:00',
                    isHide: true
                  },
                  {
                    label: '04:00',
                    isHide: true
                  },
                  {
                    label: '05:00',
                    isHide: true
                  }
                ],
              }
            }
            },
            methods: {
              callbackRange: function(val) {
                this.rangeValue = val
              }
            }
          }
        
</script>