<template>
    <div>
        <router-view />
    </div>
</template>

<script>
export default {
    name: 'FullPage',
    data: () => ({

    }),
    components: ({
    }),
    // mounted() {
    //     let user = localStorage.getItem('user-info')
    //     if (!user) {
    //         this.$router.push({ name: 'Login' })
    //     }
    // }
}
</script>

<style></style>