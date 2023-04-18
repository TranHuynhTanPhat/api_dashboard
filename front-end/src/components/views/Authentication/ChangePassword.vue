<template>
    <div>hello</div>
</template>
<script>
export default {
    name: 'ChangePassword',
    data: () => {

    }, mounted() {
        if (localStorage.getItem('id') === null || localStorage.getItem('token') === null) {
            this.$router.push({ name: 'Signin' })
        }
    }
}
</script>
