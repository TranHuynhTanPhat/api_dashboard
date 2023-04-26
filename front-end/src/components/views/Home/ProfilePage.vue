<template>
  <div>
    <Navbar />
    <div class="profile">
      <div><img src="../../../assets/images/avt.jpg" alt="Avatar" /></div>
      <div>
        <p class="label">{{ lable }}</p>
      </div>
      <div>
        <p class="email">{{ email }}</p>
      </div>
      <div class="profile-bottom">
        <button @click="handleClick" class="btn-change">Change Password</button>
        <button @click="handleDelete" class="btn-delete">Delete Account</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Navbar from "../../AppNav.vue";
import { UPDATE_DELETE_USER } from "../../../axios";
export default {
  name: "ProfilePage",
  data() {
    return {
      lable: "Email:",
      email: localStorage.getItem("email"),
    };
  },
  components: {
    Navbar,
  },
  mounted() {
    if (
      localStorage.getItem("id") == null ||
      localStorage.getItem("access_token") == null
    ) {
      this.$router.push({ name: "Signin" });
    }
  },
  created() {
    this.$store.commit("isProfile");
  },
  methods: {
    handleClick() {
      this.$router.push({ name: "ChangePassword" });
    },
    async handleDelete() {
      await axios
        .put(UPDATE_DELETE_USER + "/" + localStorage.getItem("id"), {
          status: 0,
        })
        .then((res) => {
          if (res.status == 200) {
            this.$router.push({ name: "Signin" });
            localStorage.removeItem("access_token");
            localStorage.removeItem("id");
            localStorage.removeItem("email");
            localStorage.removeItem("role");
          }
        })
        .catch((ex) => {
          alert(ex);
        });
    },
  },
};
</script>

<style>
@import url("../../../assets/css/nav-style.css");
@import url("../../../assets/css/profile-style.css");
</style>