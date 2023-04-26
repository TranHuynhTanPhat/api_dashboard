<template>
  <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
  <div>
    <div class="navcontain">
      <div
        @click="handleLogin"
        class="header-name-page"
        style="cursor: pointer"
      >
        {{ msgVerify }}
      </div>
    </div>
    <div class="contain">
      <form @submit.prevent="handlerVerify">
        <input
          v-model="OTP"
          oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
          type="number"
          maxlength="6"
          required
          placeholder="Enter OTP"
        />
        <button class="login">Verify</button>
      </form>
    </div>
  </div>
</template>
  <script>
// import axios from "axios"

export default {
  name: "ForgotPassword",

  data() {
    return {
      msgVerify: "Verify",
      OTP: "",
    };
  },
  methods: {
    async handlerVerify() {
      if (this.activeOTP == "send") {
        this.activeOTP = "verify";
        // await axios.get()
      } else if (this.activeOTP == "verify") {
        this.activeOTP = "change";
        // await axios.get()
      } else {
        this.activeOTP = "send";
        console.log(this.password);
        // await axios.put()

        this.$router.push({ name: "Signin" });
      }
    },
    handleLogin() {
      this.$router.push({ name: "Signin" });
    },
  },
};
</script>
  <style>
@import url("../../../assets/css/nav-style.css");
@import "../../../assets/css/form-style.css";

form .otp {
  display: flex;
  flex-flow: row;
  justify-items: center;
  align-items: center;
  gap: 20px;
}
</style>
  
  