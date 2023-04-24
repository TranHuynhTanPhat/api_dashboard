<template>
  <div>
    <Navbar />
    <div class="changepassword">
      <div class="contain-input">
        <input type="password" :placeholder="this.label.pw" id="inputPW" required/>
        <input type="password" :placeholder="this.label.cpw" id="inputPW2" required/>
        <span id="notify-error"></span>
        <button @click.prevent="handleChange">Change</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Navbar from "../../AppNav.vue";
import { UPDATE_DELETE_USER } from "../../../axios";

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
    this.$store.commit("isProfile");
  },
  methods: {
    async handleChange() {
      var pw = document.getElementById("inputPW").value;
      var pw2 = document.getElementById("inputPW2").value;

      if (pw == pw2 && pw!="") {
        await axios.put(UPDATE_DELETE_USER + "/" + localStorage.getItem("id"), {
          password: pw,
        });
      }
      else if(pw!=" "){
        document.getElementById("notify-error").innerHTML="Enter password"

      }
      else{
        document.getElementById("notify-error").innerHTML="Password do NOT match!"
      }
      this.$router.push({name:"Profile"})
    },
  },
};
</script>

<style>
@import url("../../../assets/css/nav-style.css");
@import url("../../../assets/css/changepassword-style.css");
</style>
