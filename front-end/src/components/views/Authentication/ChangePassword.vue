<template>
  <div>
    <Navbar />
    <div class="changepassword">
      <div class="contain-input">
        <input type="password" :placeholder="this.label.pw" />
        <input type="password" :placeholder="this.label.cpw" />
        <button>Change</button>
      </div>
    </div>
  </div>
</template>
<script>
import Navbar from "../../AppNav.vue";

export default {
  name: "ChangePassword",
  data() {
    return {
      label: {
        pw: "Password",
        cpw: "Confirm password",
      },
      email: localStorage.getItem("email"),
    };
  },
  components: {
    Navbar,
  },
  mounted() {
    if (
      localStorage.getItem("id") === null ||
      localStorage.getItem("token") === null
    ) {
      this.$router.push({ name: "Signin" });
    }
  },
  created() {
    this.$store.commit("ischangepassword");
  },
};
</script>

<style scoped>
@import url("../../../assets/css/changepassword-style.css");
</style>
