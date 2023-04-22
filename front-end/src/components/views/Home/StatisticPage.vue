<template>
  <div>
    <Navbar />
    <div class="statistic-main">
      <div class="statistic-main-left">
        <p class="h1" style="margin: 5px 0 15px 20px">Inspection</p>
        <table>
          <thead>
            <th style="padding-left: 20px">ID</th>
            <th>State OK</th>
            <th>From</th>
            <th style="width: 8%">To</th>
          </thead>
          <tbody>
            <tr
              v-for="item in sortListData"
              :key="item.id"
              @click="getDetail(item.id)"
            >
              <td>
                <p class="content">{{ item["id"] }}</p>
              </td>
              <td v-if="item['state_ok'] < 20">
                <p style="color: red; font-weight: 800">
                  {{ item["state_ok"] }}%
                </p>
              </td>
              <td v-else-if="item['state_ok'] > 50">
                <p style="color: rgb(0, 123, 255)">{{ item["state_ok"] }}%</p>
              </td>
              <td v-else>
                <p>{{ item["state_ok"] }}%</p>
              </td>
              <td>
                <p>{{ item["begin"] }}</p>
              </td>
              <td>
                <p>{{ item["end"] }}</p>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="footer-table">
          <button @click="prevPage">
            <font-awesome-icon
              icon="fa-solid fa-chevron-left"
              size="2xl"
              style="color: #3d5554"
            />
          </button>
          <p>{{ this.currentPage }}</p>
          <button @click="nextPage">
            <font-awesome-icon
              icon="fa-solid fa-chevron-right"
              size="2xl"
              style="color: #3d5554"
            />
          </button>
        </div>
      </div>
      <div
        class="statistic-main-right"
        v-if="this.$store.state.chartDashboard.angleId != null"
      >
        <DoughnutChart/>
      </div>
      <div class="statistic-main-right" v-else>
        <p class="note">Click row to show chart !</p>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { GET_INSPECTION, GET_INSPECTION_DETAIL } from "@/axios";
import Navbar from "../../AppNav.vue";
import DoughnutChart from "./charts/DoughnutChart.vue";

export default {
  name: "StatisticPage",
  components: {
    Navbar,
    DoughnutChart,
  },
  data() {
    return {
      listInspection: [],
      pageSize: 10,
      currentPage: 1,
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
    this.$store.commit("isStatistic");

    await axios.get(GET_INSPECTION).then((res) => {
      if (res.status == 200) {
        this.listInspection = res.data.data;
      }
    });
  },
  methods: {
    nextPage() {
      if (this.currentPage * this.pageSize < this.listInspection.length)
        this.currentPage++;
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
    async getDetail(id) {
      console.log(id);
      await axios
        .get(GET_INSPECTION_DETAIL, { params: { id: id } })
        .then((res) => {
          if (res.status == 200) {
            this.$store.dispatch("angleId", res.data.angle_id);
          }
        })
        .catch((ex) => console.log(ex));
    },
  },
  computed: {
    sortListData() {
      return this.listInspection.filter((row, index) => {
        let start = (this.currentPage - 1) * this.pageSize;
        let end = this.currentPage * this.pageSize;
        if (index >= start && index < end) return true;
      });
    },
  },
};
</script>
<style scoped>
@import url("../../../assets/css/statistic-style.css");
</style>