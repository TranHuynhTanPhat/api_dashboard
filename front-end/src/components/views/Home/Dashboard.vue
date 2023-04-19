<template>
  <div>

    <Navbar />
    <div class="dashboard-contain-top">
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">today's users</p>
          <p class="main">1,500</p>
          <div class="desc">
            <p class="desc-percent">2%</p>
            <p class="desc-content">since last week</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #065083;">
          <font-awesome-icon icon="fa-solid fa-users" size="2xl" style="color:white" />
        </div>
      </div>
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">new client</p>
          <p class="main">500</p>
          <div class="desc">
            <p class="desc-percent">-1%</p>
            <p class="desc-content">since last quarter</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #fe8f21;">
          <font-awesome-icon icon="fa-solid fa-user-plus" size="2xl" style="color:white" />
        </div>
      </div>
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">Status Success</p>
          <p class="main">1,500</p>
          <div class="desc">
            <p class="desc-percent">2%</p>
            <p class="desc-content">compared to failure</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #007bff;">
          <font-awesome-icon icon="fa-solid fa-globe" size="2xl" style="color:white" />
        </div>
      </div>
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">Status failure</p>
          <p class="main">1,000</p>
          <div class="desc">
            <p class="desc-percent">2%</p>
            <p class="desc-content">since yesterday</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: red;">
          <font-awesome-icon :icon="['fas', 'circle-info']" size="2xl" style="color:white" />
        </div>
      </div>
    </div>

    <div class="dashboard-contain-main">
        <div class="contain-main-child-left"></div>
        <div class="contain-main-child-right"></div>
    </div>
  </div>
</template>
<script>

import Navbar from '../../AppNav.vue'
export default {
  name: "DashboardPage",
  data() {
    return {

    }
  }, components: {
    Navbar,
  },
  mounted() {
    if (localStorage.getItem('id') === null || localStorage.getItem('token') === null) {
      this.$router.push({ name: 'Signin' })
    }
  },
  created() {
    document.title = "Dashboard"
    this.$store.commit('isDashboard');
  }
}
</script>
<style scoped>
@import url('../../../assets/css/dashboard-style.css');
</style>