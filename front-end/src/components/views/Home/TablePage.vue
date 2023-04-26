<template>
  <div>
    <Navbar />
    <div class="table-main">
      <div class="table-main-top">
        <div class="table-main-top-left">
          <AlertDialog :show="this.show" @close="close" @load-user="loadUser" />
          <download-excel
            class="btn btn-default"
            :data="listUsers"
            :fields="json_fields"
            worksheet="Users"
            name="users.xls"
          >
            <div class="h1" style="margin: 5px 0 15px 20px; width: fit-content">
              <font-awesome-icon
                icon="fa-solid fa-file-excel"
                style="color: #026600"
                size="2xl"
                class="btn-export"
              />
              List User
            </div>
          </download-excel>
          <table>
            <thead>
              <th style="padding-left: 20px">ID</th>
              <th>Email</th>
              <th>Status</th>
              <th>Role</th>
              <th>Accessed_at</th>
              <th>Created_at</th>
              <th
                style="
                  text-align: center;
                  vertical-align: middle;
                  padding-right: 10px;
                "
              >
                <button
                  style="
                    color: #3d5554;
                    padding: 5px 5px;
                    background-color: #3d55544c;
                    border-radius: 10px;
                  "
                  @click="handleAddAlert"
                >
                  + Add User
                </button>
              </th>
            </thead>
            <tbody>
              <tr v-for="item in sortListUsers" :key="item.id">
                <td @click="handleClick(item)">
                  <p class="content-start">{{ item["id"] }}</p>
                </td>
                <td @click="handleClick(item)">
                  <p>{{ item["email"] }}</p>
                </td>
                <td @click="handleClick(item)">
                  <p>{{ item["status"] }}</p>
                </td>
                <td @click="handleClick(item)">
                  <p>{{ item["role"] }}</p>
                </td>
                <td @click="handleClick(item)">
                  <p>
                    {{ item["accessed_at"]["date"] }} at
                    {{ item["accessed_at"]["time"] }}
                  </p>
                </td>
                <td @click="handleClick(item)">
                  <p>
                    {{ item["created_at"]["date"] }} at
                    {{ item["created_at"]["time"] }}
                  </p>
                </td>
                <td
                  style="
                    text-align: center;
                    vertical-align: middle;
                    padding-right: 10px;
                  "
                >
                  <button
                    @click.prevent="handleDelete(item['id'])"
                    style="padding: 0 10px"
                  >
                    <font-awesome-icon
                      icon="fa-solid fa-trash"
                      size="xl"
                      style="color: #ff0000"
                    />
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
          <div
            class="footer-table"
            v-if="this.listUsers.length > this.pageSize"
          >
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
        <div
          class="table-main-top-right"
          v-if="this.currentUser != 'Undefined'"
        >
          <div class="form-update">
            <div class="form-input">
              <label for="email">Email:</label>
              <input
                type="email"
                :placeholder="this.currentUser['email']"
                name="email"
                id="inputEmail"
              />
            </div>
            <div class="form-input">
              <label for="status">Status:</label>
              <input
                type="number"
                :placeholder="this.currentUser['status']"
                name="status"
                id="inputStatus"
                oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength); if(this.value!=1 && this.value!=0) this.value=''"
                maxlength="1"
              />
            </div>
            <button @click.prevent="handleUpdate">Update</button>
          </div>
        </div>
        <div class="table-main-top-rignt" v-else>
          <p class="note">Click row to update user !</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { UPDATE_DELETE_USER } from "../../../axios";
import Navbar from "../../AppNav.vue";
import { GET_USER } from "@/axios";

import AlertDialog from "@/components/views/Home/AlertDialog.vue";

export default {
  name: "TablePage",
  data() {
    return {
      listUsers: [],
      pageSize: 10,
      currentPage: 1,
      currentUser: "Undefined",
      show: false,
      json_fields: {
        ID: "id",
        Email: "email",
        Status: "status",
        Accessed_at: {
          field: "accessed_at",
          callback: (value) => {
            if (value.date != "NaN") return value.date + " at " + value.time;
          },
        },
        Created_at: {
          field: "created_at",
          callback: (value) => {
            return value.date + " at " + value.time;
          },
        },
      },
      json_meta: [
        [
          {
            key: "charset",
            value: "utf-8",
          },
        ],
      ],
    };
  },
  components: {
    Navbar,
    AlertDialog,
  },
  mounted() {
    // localStorage.getItem("role") != 0
    if (
      localStorage.getItem("id") == null ||
      localStorage.getItem("access_token") == null
    ) {
      this.$router.push({ name: "Signin" });
    }
  },
  async created() {
    this.$store.commit("isTable");

    this.loadUser();
  },
  methods: {
    nextPage() {
      if (this.currentPage * this.pageSize < this.listUsers.length)
        this.currentPage++;
    },
    prevPage() {
      if (this.currentPage > 1) this.currentPage--;
    },
    handleClick(item) {
      if (item == this.currentUser) {
        this.currentUser = "Undefined";
      } else {
        this.currentUser = item;
      }
      document.getElementById("inputStatus").value = "";
    },
    async handleUpdate() {
      var ipEmail = document.getElementById("inputEmail").value;
      var ipStatus = document.getElementById("inputStatus").value;

      if (ipEmail != "") {
        this.currentUser["email"] = ipEmail;
      }
      if (ipStatus != "") {
        this.currentUser["status"] = ipStatus;
      }

      await axios.put(UPDATE_DELETE_USER + "/" + this.currentUser["id"], {
        email: this.currentUser["email"],
        status: this.currentUser["status"],
      });
    },
    async handleDelete(id) {
      await axios
        .delete(UPDATE_DELETE_USER + "/" + id)
        .then((this.currentUser = "Undefined"))
        .catch((ex) => console.log(ex));
      await axios.get(GET_USER).then((res) => {
        if (res.status == 200) {
          this.listUsers = res.data.data;
        }
      });
    },
    handleAddAlert() {
      this.show = true;
    },
    close() {
      this.show = false;
    },
    async loadUser() {
      await axios.get(GET_USER).then((res) => {
        if (res.status == 200) {
          this.listUsers = res.data.data;
        }
      });
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
@import url("../../../assets/css/table-style.css");
</style>