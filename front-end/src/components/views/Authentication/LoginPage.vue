<template>
  <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
  <div>
    <div class="navcontain">
      <div class="header-name-page" @click="handleHome" style="cursor: pointer">
        {{ msgLogin }}
      </div>
    </div>
    <div class="contain">
      <form @submit.prevent="handlerSubmit">
        <div>
          <img
            src="../../../assets/images/admin01.png"
            alt="Login"
            width="100px"
            height="100px"
          />
        </div>
        <input type="text" v-model="email" placeholder="Enter Email" required />
        <input
          type="password"
          v-model="password"
          placeholder="Enter Password"
          required
        />
        <span id="messError"></span>

        <button>Sign in</button>
        <div class="text-contain">
          <div class="forgotpassword">
            <div
              @click="handleForgotPW"
              style="font-style: italic; cursor: pointer;"
            >
              Forgot password?
            </div>
          </div>
          <div class="donthavaaccount">
            Don't have account?
            <router-link to="/auth/register">
              <div
                style="
                  font-weight: 500;
                  font-size: 14px;
                  line-height: 16px;
                  display: flex;
                  align-items: center;
                "
              >
                Sign up
              </div>
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { LOGIN } from "@/axios";

export default {
  name: "LoginPage",

  data() {
    return {
      msgLogin: "Log in into API DASHBOARD",
      email: "",
      password: "",
    };
  },
  computed: {},
  methods: {
    async handlerSubmit() {
      await axios
        .post(LOGIN, { email: this.email, password: this.password })
        .then((res) => {
          if (res.status == 200) {
            localStorage.setItem("id", res.data.data.id);
            localStorage.setItem("email", res.data.data.email);
            localStorage.setItem("role", res.data.data.role);
            localStorage.setItem("access_token", res.data.access_token);

            axios.defaults.headers.common[
              "Authorization"
            ] = `Bearer ${res.data.access_token}`;

            this.$router.push({ name: "Dashboard" });
          }
        })
        .catch((ex) => {
          console.log(ex);
          if (ex.response.status == 401) {
            document.getElementById("messError").innerHTML =
              "Email or password is invalid!";
          }
          if (ex.response.status == 404) {
            document.getElementById("messError").innerHTML =
              "Account's been deleted. Contact us to restore!";
          }
        });
    },
    handleForgotPW() {
      console.log("a");
      alert("Contact us to reset password");
    },
    handleHome() {
      this.$router.push({ name: "Introduction" });
    },
  },
  created() {
    localStorage.removeItem("access_token");

    localStorage.removeItem("id");
    localStorage.removeItem("email");
    localStorage.removeItem("role");
  },
};
</script>
<style>
@import url("../../../assets/css/nav-style.css");
@import "../../../assets/css/form-style.css";

.text-contain .forgotpassword a:hover {
  color: #3d55547a;
}
</style>

