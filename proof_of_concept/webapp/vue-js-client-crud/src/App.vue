<!--
  Project Name: GDP- Gathering Detection Platform
  File Name: mainPage.vue
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file containes the code related to all the components presents in the webapp.
  Last change date: 2021-05-16
-->


<template>
  <div id="barAndFooter">
    <div id="noFooter">
      <h1>GDP: Gathering Detection Platform</h1>
      <div id="navsearch">
        <nav id="navbar" class="navbar navbar-expand navbar-light bg-light"> <!-- -->
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <router-link to="/">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/chiSiamo">Chi siamo</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/confrontoCittà">Confronto di città</router-link>
              </li>
              <li>
                <a :href="pdfLink" download="download">Manuale Utente</a>
              </li>
            </ul>
            <autosearch />
          </div>
        </nav>
      </div>
      <router-view />
    </div>

    <footer class="bg-light text-center text-lg-start  mt-auto">
      <div class="container p-4">
        <div class="row">
          <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
            <h5 class="text-uppercase">GDP</h5>
            <p>
              Web application del progetto GDP - Gathering detection platform
            </p>
          </div>
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase">Links</h5>
            <ul class="list-unstyled mb-0">
              <li>
                <a href="https://www.synclab.it/">Sync Lab</a>
              </li>
            </ul>
          </div>
          <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
            <h5 class="text-uppercase ">Contatti</h5>
            <ul class="list-unstyled mb-0">
              <li>
                <a href="mailto: jawadruids@gmail.com">jawadruids@gmail.com</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div
        class="text-center p-3"
        style="background-color: rgba(0, 0, 0, 0.2);"
      >
        © 2020 Copyright:
        <a href="https://mdbootstrap.com/">MDBootstrap.com</a>
      </div>
    </footer>
  </div>
</template>

<script>
import autosearch from "./components/autocompleteSearch.vue";
import router from "./router.js";

export default {
  name: "app",
  router: router,
  data() {
    return {
      pdfLink: require("@/assets/manuale_utente.pdf"),
    };
  },
  components: {
    autosearch,
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

h1 {
  font-weight: bold;
  font-size: 2.5em;
  padding: 0.3em;
  position: relative;
  text-align: center;
  font-style: italic;
  margin: auto;
}

#barAndFooter {
  max-width: none;
  margin: auto;
}

#noFooter ul li {
  padding-left: 10%;
  padding-right: 10%;
  width: 100%;
}
#noFooter ul {
  width: 80%;
  margin-right: 1px !important;
}
footer {
  /* bottom: 0em; */
  width: 100%;
  /* margin-bottom: 0em; */
}
#noFooter {
  /* position: relative; */
  min-height: 70vh;
  padding-bottom: 2em;
  display: block;
  z-index: 0;
}

#navbar {
  width: 100%;
  /* flex-flow: row nowrap;
  justify-content: flex-start; */
}

#navsearch {
  display: flex;
}

#navbarSupportedContent ul li{
  width: 40%;
  padding-left: 2%;
  padding-right: 2%;
}

a {
  color: blue;
}
</style>
