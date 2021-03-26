<template>
  <div id="app">
    <div id="noFooter">
      <h1>GDP: Gathering Detection Platform</h1>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">Home</li>
          <li class="nav-item">
            <router-link to="/chiSiamo">Chi siamo</router-link>
          </li>
          <li class="nav-item dropdown">link alle città</li>
        </ul>
      </div>
      </nav>
      <div>
          <autosearch/>
          </div>
    <mainPage/>
  </div>

    <footer class="bg-light text-center text-lg-start  mt-auto">
        <div class="container p-4">
        <div class="row">
      <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
        <h5 class="text-uppercase">Footer Content</h5>
          <p>
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iste atque ea quis
            molestias. Fugiat pariatur maxime quis culpa corporis vitae repudiandae aliquam
            voluptatem veniam, est atque cumque eum delectus sint!
          </p>
      </div>
      <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
        <h5 class="text-uppercase">Links</h5>

        <ul class="list-unstyled mb-0">
          <li>
            <a href="https://www.synclab.it/" class="text-dark">Sync Lab</a>
          </li>
        </ul>
      </div>
      <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
        <h5 class="text-uppercase mb-0">Contatti</h5>
        <ul class="list-unstyled">
          <li>
            <a href = "mailto: jawadruids@gmail.com">jawadruids@gmail.com</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    © 2020 Copyright:
    <a class="text-dark" href="https://mdbootstrap.com/">MDBootstrap.com</a>
  </div>

  </footer>
  </div>
</template>

<script>
import mainPage from './components/mainPage.vue'
import autosearch from './components/autocompleteSearch.vue'

export default {
  name: 'app',
  components: {
    mainPage,
    autosearch
  }
}
</script>

<style scoped>
h1 {
 position: relative;
 text-align: center;
}
#app ul li{
  padding-left:10%;
  padding-right:10%;
  width:100%;
}
#app ul{
  width: 80%;
}
footer{
  bottom: 0em;   
  width: 100%;
  margin-bottom: 0em;
}
#noFooter{
  position: relative;
  min-height: 100vh;
  padding-bottom: 10em;
  display: block;
}


</style>
