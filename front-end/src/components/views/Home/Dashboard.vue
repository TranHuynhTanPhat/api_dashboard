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
        <div class="contain-top-child-right">

        </div>
      </div>

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

.dashboard-contain-top {
  margin-top: 120px;
  display: flex;
  flex-flow: row;
  justify-content: center;
  align-items: center;
  flex-wrap: nowrap;


  gap: 50px;

}

.dashboard-contain-top .contain-top-child {
  background-color: white;

  padding: 20px;

  width: auto;
  height: auto;

  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;

  border-radius: 15px;
}

.contain-top-child-left {
  height: auto;
  width: 200px;

  display: flex;
  flex-flow: column;
  justify-content: flex-start;
  align-items:start;;
  gap: 5px;
}

.contain-top-child-right {
  height: auto;
  width: 50px;
}


.contain-top-child-left .title {
  text-transform: uppercase;
  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  color: #3d5554b9;
}

.contain-top-child-left .main {
  text-transform: uppercase;
  font-style: normal;
  font-weight: 800;
  font-size: 28px;
  color: #3d5554;
}

.contain-top-child-left .desc{
  display: flex;
  flex-flow: row;
  justify-content: start;
  align-items: start;
  margin-top: 10px;

  gap: 5px;
}

.desc .desc-percent{
  text-transform:none;
  font-style: italic;
  font-weight: 300;
  font-size: 16px;
  color: #1990B2;
}

.desc .desc-content{
  text-transform:none;
  font-style: italic;
  font-weight: 300;
  font-size: 16px;
  color: #3d5554b9;
}
</style>