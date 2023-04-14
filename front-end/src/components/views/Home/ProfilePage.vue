<template>
  <div>
    <Navbar/>
  </div>
</template>
<script>
import Navbar from '../../AppNav.vue'
export default {
  name: 'ProfilePage',
  data() {
    return {

    }
  },components:{
    Navbar
  },
  mounted() {
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
    this.$store.commit('isProfile')
  }
}
</script>

<style scoped>
@import '../../../assets/css/nav-style.css';
</style>