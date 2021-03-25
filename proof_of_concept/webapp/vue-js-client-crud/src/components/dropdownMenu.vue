<template>
<ejs-dropdownbutton :items='items' iconCss= 'ddb-icons e-message'>Message</ejs-dropdownbutton>
</template>

<script>
import Vue from 'vue';
import { DropDownButtonPlugin } from "@syncfusion/ej2-vue-splitbuttons";
import { enableRipple } from '@syncfusion/ej2-base';

enableRipple(true);
Vue.use(DropDownButtonPlugin);

export default {
    data () {
        return {
            items:[
            {
                text: 'CIAO',
            },
            {
                text: 'EMMA',
            },
            {
                text: 'ODIO',
            },
            {
                text: 'VUE',
            }]
        };
    }
}
</script>