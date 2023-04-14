<template>
  <div>
    <Navbar />
  </div>
</template>
<script>
import Navbar from '../../AppNav.vue';
export default {
  name: 'StatisticPage',
  data() {
    return {

    }
  }, components: {
    Navbar
  }, mounted() {
    // let user = localStorage.getItem('user-info')
    // console.log(user)
    // if (user === null) {
    //   this.$router.push({ name: 'Signin' })
    // }

    let user = this.$store.state
    if (user === null || localStorage.getItem("token") === null) {
      this.$router.push({ name: 'Signin' })
    }

  },
  created(){
    this.$store.commit('isStatistic')
  }

}
</script>
<style scoped>
@import url('../../../assets/css/nav-style.css');
</style>