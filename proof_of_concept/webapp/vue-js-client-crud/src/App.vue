<template>
  <div id="app">
    <mainPage/>
  </div>
</template>

<script>
import mainPage from './components/mainPage.vue'

export default {
  name: 'app',
  components: {
    mainPage
  }
}
</script>

<style scoped>
 div {
   height: 100em;
 }
</style>
