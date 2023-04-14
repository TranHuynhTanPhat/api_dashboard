<template>
  <div>
    <div class="header">
      <div class="nav">
        <div class="nav-contain">
          <div class="item"><router-link to="./profile" @click.prevent="handlerClick('profile')">
              <img src="../../../assets/images/nav_table.png" alt="">
            </router-link></div>

          <div class="item"><router-link to="./profile" @click.prevent="handlerClick('profile')">
              <img src="../../../assets/images/nav_statistic.png" alt="">
            </router-link></div>

          <div class="item"><router-link to="./profile" @click.prevent="handlerClick('profile')">
              <img src="../../../assets/images/nav_dashboard.png" alt="">
            </router-link></div>

          <div class="item"><router-link to="./profile" @click.prevent="handlerClick('profile')">
              <img src="../../../assets/images/nav_profile.png" alt="">
            </router-link></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'ProfilePage',
  data() {
    return {

    }
  },
  mounted() {
    // let user = localStorage.getItem('user-info')
    // console.log(user)
    // if (user === null) {
    //   this.$router.push({ name: 'Signin' })
    // }

    let user = this.$store.state
    if (user === null || localStorage.getItem("token") === null) {
      this.$router.push({ name: 'Signin' })
    }

  }
}
</script>

<style scoped>
.header {
  height: 120px;
  width: 100%;
  background: transparent;

  overflow: hidden;
  position: fixed;
  top: 0;


}

.nav {
  height: 60px;
  width: 100%;

  background: url('../../../assets/images/navbar_full.png');
  background-color: white;
  background-position: center;
  background-repeat: no-repeat;
  background-size: auto;

  box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 2px, rgba(0, 0, 0, 0.07) 0px 2px 4px, rgba(0, 0, 0, 0.07) 0px 4px 8px, rgba(0, 0, 0, 0.07) 0px 8px 16px, rgba(0, 0, 0, 0.07) 0px 16px 32px, rgba(0, 0, 0, 0.07) 0px 32px 64px;
}

.nav-contain {
  height: 60px;
  width: 100%;

  padding: 0px 50px 0px 50px;

  display: flex;
  flex-flow: row;
  justify-content: flex-end;
  align-items: center;
  flex-wrap: nowrap;


  gap: 50px;


}

.item {
  height: 50px;
  width: 50px;

  display: flex;
  justify-content: center;
  align-items: center;

  border-radius: 100%;

  margin: 0 5px
}

.item:hover {
  height: 60px;
  width: 60px;
  background: white;

  margin: 0px;

  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
}

img {
  height: 50px;
  width: 50px;
  border-radius: 100%;

  margin: auto;
}

img:hover {
  height: 60px;
  width: 60px;
  margin: auto;
  src: url('../../../assets/images/nav_profile_active.png');
}
</style>