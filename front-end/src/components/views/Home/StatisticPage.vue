<template>
  <div>
    <Navbar />
    <div class="statistic-main">
      <div class="statistic-main-top">
        <div class="statistic-main-top-left">
          <p class="h1" style="margin: 5px 0 15px 20px">Inspection</p>
          <table>
            <thead>
              <th style="padding-left: 20px">ID</th>
              <th>Status OK</th>
              <th>From</th>
              <th>To</th>
            </thead>
            <tbody>
              <tr
                v-for="item in sortListData"
                :key="item.id"
                @click="getDetail(item.id)"
              >
                <td>
                  <p class="content-start">{{ item["id"] }}</p>
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
                <td>
                  <p class="content-end">
                    <font-awesome-icon
                      icon="fa-solid fa-chevron-right"
                      style="color: #3d5554"
                    />
                  </p>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="footer-table" v-if="this.listInspection.length > 10">
            <button @click="prevPagePa" v-if="this.currentPagePa != 1">
              <font-awesome-icon
                icon="fa-solid fa-chevron-left"
                size="2xl"
                style="color: #3d5554"
              />
            </button>
            <p>{{ this.currentPagePa }}</p>
            <button
              @click="nextPagePa"
              v-if="this.currentPagePa * 10 < this.listInspection.length"
            >
              <font-awesome-icon
                icon="fa-solid fa-chevron-right"
                size="2xl"
                style="color: #3d5554"
              />
            </button>
          </div>
        </div>
        <div
          class="statistic-main-top-right"
          v-if="this.currentId != 'Undefined'"
        >
          <p class="h1" style="margin: 5px 0 15px 20px">{{ this.currentId }}</p>
          <table>
            <thead>
              <th style="padding-left: 20px">Date</th>
              <th>Time</th>
              <th>Angle_id</th>
              <th>Status</th>
              <th>Predict_result</th>
            </thead>
            <tbody>
              <tr v-for="item in sortListAllDetails" :key="item.id">
                <td>
                  <p class="content-start">{{ item["date"] }}</p>
                </td>
                <td>
                  <p>{{ item["time"] }}</p>
                </td>
                <td>
                  <p>{{ item["angle_id"] }}</p>
                </td>
                <td>
                  <p
                    v-if="item['status'] === 'ok'"
                    style="color: #58d68d; font-weight: 800"
                  >
                    {{ item["status"] }}
                  </p>
                  <p v-else>
                    {{ item["status"] }}
                  </p>
                </td>
                <td>
                  <p>{{ item["predict_result"] }}</p>
                </td>
              </tr>
            </tbody>
          </table>
          <div
            class="footer-table"
            v-if="this.listAllDetails.length > this.pageSize"
          >
            <button @click="prevPageCh" v-if="this.currentPageCh != 1">
              <font-awesome-icon
                icon="fa-solid fa-chevron-left"
                size="2xl"
                style="color: #3d5554"
              />
            </button>
            <p>{{ this.currentPageCh }}</p>
            <button
              @click="nextPageCh"
              v-if="this.currentPageCh * 10 < this.listAllDetails.length"
            >
              <font-awesome-icon
                icon="fa-solid fa-chevron-right"
                size="2xl"
                style="color: #3d5554"
              />
            </button>
          </div>
          <div class="footer-table" v-else style="padding-bottom: 20px"></div>
        </div>
        <div class="statistic-main-top-rignt" v-else></div>
      </div>
      <div class="statistic-main-bottom">
        <div
          class="statistic-main-bottom-content"
          v-if="this.$store.state.chartDashboard.angleId != null"
        >
          <DoughnutChart />
        </div>
        <div class="statistic-main-bottom-content" v-else>
          <p class="note">Click row to show chart !</p>
        </div>
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
      listAllDetails: [],
      pageSize: 10,
      currentPagePa: 1,
      currentPageCh: 1,
      currentId: "Undefined",
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
    this.$store.dispatch("angleId", null);

    await axios.get(GET_INSPECTION).then((res) => {
      if (res.status == 200) {
        this.listInspection = res.data.data;
      }
    });
  },
  methods: {
    nextPagePa() {
      if (this.currentPagePa * this.pageSize < this.listInspection.length)
        this.currentPagePa++;
    },
    prevPagePa() {
      if (this.currentPagePa > 1) this.currentPagePa--;
    },

    nextPageCh() {
      if (this.currentPageCh * this.pageSize < this.listAllDetails.length)
        this.currentPageCh++;
    },
    prevPageCh() {
      if (this.currentPageCh > 1) this.currentPageCh--;
    },

    async getDetail(id) {
      await axios
        .get(GET_INSPECTION_DETAIL, { params: { id: id } })
        .then((res) => {
          if (res.status == 200) {
            this.$store.dispatch("angleId", res.data.angle_id);
            this.listAllDetails = res.data.all_details;
            this.currentId = id;
          }
        })
        .catch((ex) => console.log(ex));
    },
  },
  computed: {
    sortListData() {
      return this.listInspection.filter((row, index) => {
        let start = (this.currentPagePa - 1) * this.pageSize;
        let end = this.currentPagePa * this.pageSize;
        if (index >= start && index < end) return true;
      });
    },
    sortListAllDetails() {
      return this.listAllDetails.filter((row, index) => {
        let start = (this.currentPageCh - 1) * this.pageSize;
        let end = this.currentPageCh * this.pageSize;
        if (index >= start && index < end) return true;
      });
    },
  },
};
</script>
<style scoped>
@import url("../../../assets/css/statistic-style.css");
</style>