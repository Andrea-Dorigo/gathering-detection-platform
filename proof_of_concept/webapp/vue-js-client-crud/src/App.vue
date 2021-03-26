<template>
  <div id="app">
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
        <div>
          <autosearch/>
          </div>
      </div>
      </nav>
    <mainPage/>
    <footer>
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
</style>
