<template>
  <div>
    dashboard
  </div>
</template>
<script>
export default {
  name: "DashboardPage",
  data() {
    return {

    }
  },
  mounted() {
    let user = localStorage.getItem('user-info')
    console.log(user)
    if (user === null) {
      this.$router.push({ name: 'Signin' })
    }

  }
};
</script>
