<template>
    <div>
        <div class="header"></div>
        <router-view />
        <AppFooter />
    </div>
</template>

<script>
// import axios from 'axios';
import AppFooter from '../AppFooter.vue'

var data = {
    icActive: 'dashboard'
}
export default {
    name: "MainPage",
    data() {
        return {
            data,
            msg: ""
        }
    },
    components: {
        AppFooter
    },
    methods: {
        setAction(act) {
            console.log(this.icActive)
            console.log(act)


            this.icActive = act
        },
    }
}
    // mounted() {
    //     let user = localStorage.getItem('user-info')

    // }

</script>

<style>
.header {
    height: 100px;
    width: 100%;
    background: transparent;
}
</style>