<template>
  <div>
    <nav v-if="activeNav === 'logout'">
      <ul>
        <li>
          <router-link to="/auth/register" class="important" target="_parent">{{
            msgSignUp
          }}</router-link>
        </li>
        <li>
          <router-link to="/auth/login" target="_parent">{{
            msgSignIn
          }}</router-link>
        </li>
      </ul>
    </nav>
    <nav v-else>
      <ul>
        <li>
          <div @click.prevent="handlerClick" class="important" target="_parent">
            {{ msgLogout }}
          </div>
        </li>
        <li>
          <router-link to="/dashboard" target="_parent">{{
            msgHome
          }}</router-link>
        </li>
      </ul>
    </nav>
    <div class="intro">
      <img src="../../../assets/images/intro.png" width="80%" />
    </div>
    <AppFooter />
  </div>
</template>
<script scoped>
import AppFooter from "@/components/AppFooter.vue";
export default {
  name: "IntroPage",
  data: () => ({
    msgHome: "Home",
    msgSignUp: "Sign up",
    msgSignIn: "Login",
    msgLogout: "Logout",
    activeNav: "logout",
  }),
  components: {
    AppFooter,
  },
  methods: {
    async handlerClick() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");

      localStorage.removeItem("id");
      localStorage.removeItem("email");
      localStorage.removeItem("status");
      localStorage.removeItem("role");
      this.$router.go();
    },
  },
  mounted() {
    if (
      localStorage.getItem("id") != null ||
      localStorage.getItem("access_token") != null
    ) {
      this.activeNav = "login";
    } else {
      this.activeNav = "logout";
    }
  },
};
</script>
<style>
@import url("../../../assets/css/intro-style.css");
</style>