<template>
  <div>
    <Navbar />
    <div class="table-main">
      <div class="table-contain-main">
        <p class="h1" style="margin: 5px 0 15px 20px">List Users</p>
        <table>
          <thead>
            <th style="padding-left: 20px">ID</th>
            <th>Email</th>
            <th>Status</th>
            <th>Role</th>
            <th>Accessed_at</th>
            <th>Created_at</th>
          </thead>
          <tbody>
            <tr v-for="item in sortListUsers" :key="item.id">
              <td>
                <p class="content-start">{{ item["id"] }}</p>
              </td>
              <td>
                <p>{{ item["email"] }}</p>
              </td>
              <td>
                <p>{{ item["status"] }}</p>
              </td>
              <td>
                <p>{{ item["role"] }}</p>
              </td>
              <td>
                <p>{{ item["accessed_at"] }}</p>
              </td>
              <td>
                <p>{{ item["created_at"] }}</p>
              </td>
            </tr>
          </tbody>
        </table>
        <div class="footer-table" v-if="this.listUsers.length > this.pageSize">
          <button @click="prevPage" v-if="this.currentPage != 1">
            <font-awesome-icon
              icon="fa-solid fa-chevron-left"
              size="2xl"
              style="color: #3d5554"
            />
          </button>
          <p>{{ this.currentPage }}</p>
          <button
            @click="nextPage"
            v-if="this.currentPage * 10 < this.listUsers.length"
          >
            <font-awesome-icon
              icon="fa-solid fa-chevron-right"
              size="2xl"
              style="color: #3d5554"
            />
          </button>
        </div>
        <div class="footer-table"></div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Navbar from "../../AppNav.vue";
import { GET_USER } from "@/axios";

export default {
  name: "TablePage",
  data() {
    return {
      listUsers: [],
      pageSize: 10,
      currentPage: 1,
    };
  },
  components: {
    Navbar,
  },
  mounted() {
    // localStorage.getItem("role") != 0

    if (
      localStorage.getItem("id") === null ||
      localStorage.getItem("token") === null
    ) {
      this.$router.push({ name: "Signin" });
    }
  },
  async created() {
    this.$store.commit("isTable");

    await axios.get(GET_USER).then((res) => {
      if (res.status == 200) {
        this.listUsers = res.data.data;
      }
    });
  },
  methods: {
    nextPage() {
      if (this.currentPage * this.pageSize < this.listUsers.length)
        this.currentPage++;
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
  },
  computed: {
    sortListUsers() {
      return this.listUsers.filter((row, index) => {
        let start = (this.currentPage - 1) * this.pageSize;
        let end = this.currentPage * this.pageSize;
        if (index >= start && index < end) return true;
      });
    },
  },
};
</script>
<style>
@import url("../../../assets/css/nav-style.css");
@import url('../../../assets/css/table-style.css');
</style>