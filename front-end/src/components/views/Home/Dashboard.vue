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
        <div class="contain-top-child-right" style="background-color: #065083">
          <font-awesome-icon
            icon="fa-solid fa-users"
            size="2xl"
            style="color: white"
          />
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
        <div class="contain-top-child-right" style="background-color: #fe8f21">
          <font-awesome-icon
            icon="fa-solid fa-user-plus"
            size="2xl"
            style="color: white"
          />
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
        <div class="contain-top-child-right" style="background-color: #007bff">
          <font-awesome-icon
            icon="fa-solid fa-globe"
            size="2xl"
            style="color: white"
          />
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
        <div class="contain-top-child-right" style="background-color: red">
          <font-awesome-icon
            :icon="['fas', 'circle-info']"
            size="2xl"
            style="color: white"
          />
        </div>
      </div>
    </div>
    <div class="dashboard-contain-main">
      <div class="contain-main-child-left">
        <!-- <LineChart :data="data" :options="options" /> -->
        <p class="h1">Graph of router check times by angle id</p>
        <br />
        <BarChart />
      </div>
      <div class="contain-main-child-right">
        <p class="h1">Graph of router's state by angle id</p>
        <br />
        <RadarChart />
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "../../AppNav.vue";
import RadarChart from "./charts/RardarChart.vue";
import BarChart from "./charts/BarChart.vue";
import axios from "axios";
import { CHART_DATA } from "@/axios";

export default {
  name: "DashboardPage",
  components: {
    Navbar,
    RadarChart,
    BarChart,
  },
  data() {
    return {
    };
  },
  mounted() {
    if (
      localStorage.getItem("id") === null ||
      localStorage.getItem("token") === null
    ) {
      this.$router.push({ name: "Signin" });
    }
  },
  async created() {
    document.title = "Dashboard";
    this.$store.commit("isDashboard");

    const { data } = await axios.get(CHART_DATA);

    this.$store.dispatch("count", data.count);
    this.$store.dispatch("stateOk", data.stateOk);
    this.$store.dispatch("stateFail", data.stateFail);
  },
};
</script>
<style scoped>
@import url("../../../assets/css/dashboard-style.css");
</style>