import Vue from "vue";
import Router from "vue-router";

import chiSiamo from "./components/aboutUs.vue";
import mainPage from "./components/mainPage.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "mainPage",
      component: mainPage,
    },
    {
      path: "/chiSiamo",
      name: "chiSiamo",
      component: chiSiamo,
    },
  ],
});
