<template>
  <div id="chiSiamo">
      <h1>Chi siamo</h1>
      <h2>bellaaaaaa</h2>
  </div>
</template>

<script>

import router from '../router.js'

export default {
    name: 'chiSiamo',
    methods: {
            navigate() {
                window.alert("ciamo emma");
                router.push({ name: "chiSiamo" });
            }
        }
}
</script>
