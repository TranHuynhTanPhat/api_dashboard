<template>
  <div>
    <div class="header">
      <div class="nav">
        <div class="nav-contain-left">
          <div class="item" :class="{ active: isSetting }"><router-link to="/setting"><img src="../assets/images/setting.png"
                alt="Setting"></router-link></div>
        </div>
        <div class="nav-contain-right">
          <div class="item" :class="{ active: isTable }" v-if="role==0"><router-link to="./table">
              <img src="../assets/images/nav_table.png" alt="Table">
            </router-link></div>

          <div class="item" :class="{ active: isStatistic }"><router-link to="./statistic">
              <img src="../assets/images/nav_statistic.png" alt="Statistic">
            </router-link></div>

          <div class="item" :class="{ active: isDashboard }"><router-link to="./dashboard">
              <img src="../assets/images/nav_dashboard.png" alt="Dashboard">
            </router-link></div>

          <div class="item" :class="{ active: isProfile }"><router-link to="./profile">
              <img src="../assets/images/nav_profile.png" alt="Profile">
            </router-link></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>



export default {
  name: "NavPage",
  data() {
    return {
      isProfile: this.$store.state.nav.isProfile,
      isDashboard: this.$store.state.nav.isDashboard,
      isStatistic: this.$store.state.nav.isStatistic,
      isTable: this.$store.state.nav.isTable,
      isSetting: this.$store.state.nav.isSetting,
      role:localStorage.getItem("role")
    }
  },
  computed: {

  }
};
</script>
<style scoped>
@import '../assets/css/nav-style.css';
</style>