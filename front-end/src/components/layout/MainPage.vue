<template>
    <div>
        <router-view />
        <AppFooter/>
    </div>
</template>

<script>
// import axios from 'axios';
import AppFooter from '../AppFooter.vue'

export default {
    name: "MainPage",
    data() {
        return {
            msg: ""
        }
    },
    components: {
        AppFooter,
    },
    methods: {
    },
}
</script>