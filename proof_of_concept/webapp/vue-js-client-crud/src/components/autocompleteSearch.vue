<template>
  <div>
    <advanced-search :inline="true" :options="options"></advanced-search>
  </div>
</template>

<script>

  import AdvancedSearch from 'vue-advanced-search'

  export default {
    name: 'searchMio',
    components: { AdvancedSearch },
    data () {
      return {
        model: null,
        options: [
            { label: 'roma', value: 'milano' },
            { label: 'venezia', value: 'padova' }
        ]
      }
    }
  }
</script>