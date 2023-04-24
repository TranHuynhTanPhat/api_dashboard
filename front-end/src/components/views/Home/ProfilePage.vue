<template>
  <div>
    <Navbar />
    <div class="profile" >
      <div><img src="../../../assets/images/avt.jpg" alt="Avatar"></div>
      <div>
        <p class="label">{{ lable }}</p>
      </div>
      <div>
        <p class="email">{{ email }}</p>
      </div>
      <button @click="handleClick">Change Password</button>
    </div>
  </div>
</template>
<script>
import Navbar from '../../AppNav.vue'
export default {
  name: 'ProfilePage',
  data() {
    return {
      lable: "Email:",
      email: localStorage.getItem('email'),
    }
  }, components: {
    Navbar
  },
  mounted() {
    if (localStorage.getItem('id') === null || localStorage.getItem('token') === null) {
      this.$router.push({ name: 'Signin' })
    }

  },
  created() {
    this.$store.commit('isProfile')
  },
  methods:{
    handleClick(){
      this.$router.push({name:"ChangePassword"})
    }
  }
}
</script>

<style>
@import url("../../../assets/css/nav-style.css");
@import url('../../../assets/css/profile-style.css');
</style>