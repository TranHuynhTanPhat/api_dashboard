<template>
  <div>
    <Navbar />
    <div class="profile" >
      <div><img src="../../../assets/images/avt.jpg" alt="Avatar"></div>
      <div>
        <p class="label">{{ lable }}</p>
      </div>
      <div>
        <p class="email">{{ email }}</p>
      </div>
      <button>Change Password</button>
    </div>
  </div>
</template>
<script>
import Navbar from '../../AppNav.vue'
export default {
  name: 'ProfilePage',
  data() {
    return {
      lable: "Email:",
      email: this.$store.state.user.user.email,
    }
  }, components: {
    Navbar
  },
  mounted() {
    // let user = localStorage.getItem('user-info')
    // console.log(user)
    // if (user === null) {
    //   this.$router.push({ name: 'Signin' })
    // }

    let user = this.$store.state.user.user
    console.log(user.email)

    if (typeof user.id === "undefined" || localStorage.getItem("token") === null) {
      this.$router.push({ name: 'Signin' })
    }

  },
  created() {
    this.$store.commit('isProfile')
  }
}
</script>

<style scoped>
@import '../../../assets/css/nav-style.css';

.profile{
  height: 525px;
  width: 700px;

  margin: auto;
  margin-top: 100px;

  background: url('../../../assets/images/form_profile.png'), #ffffff;
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;

  display: flex;
  flex-direction: column;
  padding: 50px 100px;
}

.profile div img {
  height: 180px;
  width: 180px;

  border-radius: 100%;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
}

.label {
  font-size: 24px;
  font-weight: 700;
  color: #3D5554;


  margin-top: 40px;
  margin-left: 40px;
}

.email {
  font-size: 18px;
  font-weight: 400;
  color: #3D5554;


  margin-left: 40px;
}

.profile button{
  height: 50px;
  width: 150px;

  border-radius: 10px;

  font-size: 14px;
  font-weight: 700;
  color: white;
  background: #C99C33;

  white-space: normal;

  margin-top: 40px;
}
</style>