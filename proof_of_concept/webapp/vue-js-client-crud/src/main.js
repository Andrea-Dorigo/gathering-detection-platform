import Vue from "vue";
import App from "./App.vue";
import Trend from "vuetrend";
import router from "./router.js";

Vue.config.productionTip = false;
Vue.use(Trend);

new Vue({
  router : router,
  render: (h) => h(App),
}).$mount("#app");
