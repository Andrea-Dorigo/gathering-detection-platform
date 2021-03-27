import Vue from 'vue'
import App from './App.vue'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyC6moJ8jzEmZ3p58cdHHDQ0r-vhJ1srb_A',
    libraries: 'places',
  }
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
