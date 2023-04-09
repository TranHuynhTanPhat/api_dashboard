<template>
    <div>
        <router-view />
        <footer>
            <AppFooter />
        </footer>
    </div>
</template>

<script>
import AppFooter from '../AppFooter.vue';
export default {
    name: 'FullPage',
    data: () => ({

    }),
    components: ({
        AppFooter,
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