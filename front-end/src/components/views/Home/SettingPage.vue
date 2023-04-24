<template>
  <div>
    <Navbar />
  </div>
</template>
<script>
import Navbar from '../../AppNav.vue'
export default {
  name: 'SettingPage',
  data() {
    return {

    }
  },
  components: {
    Navbar
  }, mounted() {
    if (localStorage.getItem('id') === null || localStorage.getItem('token') === null) {
      this.$router.push({ name: 'Signin' })
    }

  },
  created() {
    this.$store.commit('isSetting')
  }
}
</script>
<style>
@import url("../../../assets/css/nav-style.css");
</style>
