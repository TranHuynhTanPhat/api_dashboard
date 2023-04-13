<template>
    <div>
    </div>
</template>
<script>
export default {
    name:'ProfilePage',
    data:()=>{
        
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
