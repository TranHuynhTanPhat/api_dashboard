<template>
  <div>
    <Navbar />
    <div class="dashboard-contain-top">
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">today's users</p>
          <p class="main">{{ this.today_user.count }}</p>
          <div class="desc" v-if="this.today_user.total === false">
            <p class="desc-percent">{{ this.today_user.percent }}%</p>
            <p class="desc-content">since last week</p>
          </div>
          <div class="desc" v-else>
            <p class="desc-percent">{{ this.today_user.percent }}%</p>
            <p class="desc-content">compared with total</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #DE3163">
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
          <p class="main">{{ this.new_clients.newClients }}</p>
          <div class="desc" v-if="this.new_clients.percent != -1">
            <p class="desc-percent">{{ this.new_clients.percent }}%</p>
            <p class="desc-content">since last quarter</p>
          </div>
          <div class="desc" v-else>
            <p class="desc-percent"></p>
            <p class="desc-content">In this quarter</p>
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
          <p class="main">{{ this.state_ok.state }}</p>
          <div class="desc">
            <p class="desc-percent">{{ this.state_ok.percent }}%</p>
            <p class="desc-content">compared with total</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #2e8364">
          <font-awesome-icon
            icon="fa-solid fa-globe"
            size="2xl"
            style="color: white"
          />
        </div>
      </div>
      <div class="contain-top-child">
        <div class="contain-top-child-left">
          <p class="title">Total check times</p>
          <p class="main">{{ this.total_check_time.total }}</p>
          <div class="desc">
            <p class="desc-percent"></p>
            <p class="desc-content">To {{ this.total_check_time.time }}</p>
          </div>
        </div>
        <div class="contain-top-child-right" style="background-color: #007bff">
          <font-awesome-icon
            icon="fa-solid fa-clipboard-check"
            size="2xl"
            style="color: white"
          />
        </div>
      </div>
    </div>
    <div class="dashboard-contain-main">
      <div class="contain-main-child-left">
        <!-- <LineChart :data="data" :options="options" /> -->
        <p class="h1">Check times by angle id</p>
        <br />
        <BarChart />
      </div>
      <div class="contain-main-child-right">
        <p class="h1">Router's state by angle id</p>
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
import {
  CHART_DATA,
  TODAY_USERS,
  NEW_CLIENTS,
  STATE_OK,
  TOTAL_CHECK_TIME,
} from "@/axios";

export default {
  name: "DashboardPage",
  components: {
    Navbar,
    RadarChart,
    BarChart,
  },
  data() {
    return {
      today_user: {
        count: 0,
        percent: 0,
        total: false,
      },
      new_clients: {
        newClients: 0,
        percent: 0,
        total: false,
      },
      state_ok: {
        state: 0,
        percent: 0,
      },
      total_check_time: {
        interval: null,
        time: null,
        total: 0,
      },
    };
  },
  mounted() {
    if (
      localStorage.getItem("id") == null ||
      localStorage.getItem("access_token") == null
    ) {

      this.$router.push({ name: "Signin" });
    }
  },
  beforeDestroy() {
    // prevent memory leak
    clearInterval(this.total_check_time.interval);
  },
  async created() {
    document.title = "Dashboard";
    this.$store.commit("isDashboard");

    console.log(localStorage.getItem("access_token"))

    this.total_check_time.today = new Date().toLocaleString();

    await axios
      .get(TODAY_USERS,{
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`
          }
        })
      .then((res) => {
        if (res.status == 200) {
          this.today_user.count = res.data.todayUsers;
          this.today_user.percent = res.data.percent;
          this.today_user.total = res.data.total;
        }
      })
      .catch((ex) => {
        console.log(ex);
      });

    await axios
      .get(NEW_CLIENTS)
      .then((res) => {
        if (res.status == 200) {
          this.new_clients.newClients = res.data.newClients;
          this.new_clients.percent = res.data.percent;
        }
      })
      .catch((ex) => {
        console.log(ex);
      });

    await axios
      .get(STATE_OK)
      .then((res) => {
        if (res.status == 200) {
          this.state_ok.state = res.data.state_ok;
          this.state_ok.percent = res.data.percent;
        }
      })
      .catch((ex) => {
        console.log(ex);
      });

    await axios
      .get(TOTAL_CHECK_TIME)
      .then((res) => {
        if (res.status == 200) {
          this.total_check_time.total = res.data.total_check;
        }
      })
      .catch((ex) => {
        console.log(ex);
      });

    const { data } = await axios.get(CHART_DATA);

    this.$store.dispatch("count", data.count);
    this.$store.dispatch("stateOk", data.stateOk);
    this.$store.dispatch("stateFail", data.stateFail);

    // update the time every second
    this.total_check_time.interval = setInterval(() => {
      // Concise way to format time according to system locale.
      // In my case this returns "3:48:00 am"
      this.total_check_time.time = Intl.DateTimeFormat(navigator.language, {
        year: "numeric",
        month: "numeric",
        date: "numeric",
        hour: "numeric",
        minute: "numeric",
        second: "numeric",
      }).format();
    }, 1000);
  },
};
</script>
<style>
@import url("../../../assets/css/nav-style.css");
@import url("../../../assets/css/dashboard-style.css");
</style>