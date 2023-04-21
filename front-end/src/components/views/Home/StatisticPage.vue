<template>
  <div>
    <Navbar />
    <div class="statistic-main">
      <div class="statistic-main-left">
        <p class="h1" style="margin: 5px 0 15px 20px">Inspection</p>
        <table>
          <thead>
            <th style="padding-left: 20px;">ID</th>
            <th>State OK</th>
            <th>From</th>
            <th>To</th>
          </thead>
          <tbody>
            <tr v-for="item in sortListData" :key="item.id">
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
      <div class="statistic-main-right"></div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { GET_INSPECTION } from "@/axios";
import Navbar from "../../AppNav.vue";

export default {
  name: "StatisticPage",
  components: {
    Navbar,
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
      this.listInspection = res.data.data;
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
.statistic-main {
  height: auto;
  width: 100%;

  margin-top: 120px;

  padding: 20px 50px;

  display: flex;
  flex-flow: row;
  justify-content: center;
  align-items: center;
  flex-wrap: nowrap;

  gap: 20px;
}

.statistic-main .statistic-main-left {
  height: 660px;
  width: 70%;

  padding: 20px 0 0 0;

  background-color: white;

  box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
    rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;

  border-radius: 15px;
}

.statistic-main .statistic-main-right {
  height: 660px;
  width: 30%;

  padding: 20px;

  background-color: white;

  box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
    rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;

  border-radius: 15px;
}

.statistic-main-left table {
  width: 100%;
  height: auto;

  text-align: left;

  border-collapse: collapse;
}

.statistic-main-left th {
  text-transform: uppercase;
  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  color: #3d555426;

  padding: 15px 0 15px 0;
}

.statistic-main-left td {
  padding: 15px 0 15px 0;

  font-weight: 500;
  color: #3d5554;

  border-top: solid 0.5px #3d555426;
}

.statistic-main-left tr:hover {
  background-color: #3d55542d;
}

.content {
  margin-left: 10px;
}

.footer-table {
  display: flex;
  flex-flow: row;
  justify-content: center;
  align-items: center;

  gap: 10px;

  padding: 15px 0 20px 0;
}

.footer-table p {
  padding: 10px;
  border-radius: 5px;
  background-color: #3d55542d;

  font-weight: 600;
  font-size: 12px;
  color: #3d5554;
}

.footer-table button{
  padding:5px;
}

.h1 {
  font-size: 24px;
  font-weight: 800;
  color: #3d5554;
}
</style>