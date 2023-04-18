<template>
  <div>
    <router-view />
  </div>
</template>
<script>

export default ({
  name: "App",
  data: () => ({
  }),
  created() {
    document.title = "API Dashboard"
  }
})
</script>


<style lang="scss"></style>
