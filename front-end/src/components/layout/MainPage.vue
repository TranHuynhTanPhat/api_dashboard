<template>
    <div>
        <div>
            <!-- <b-nav>
                <b-nav-item active><router-link to="/dashboard">
                        <div v-if="dashboard"><img src="../../assets/images/nav_dashboard_active.png" alt="Dashboard"></div>
                        <div v-else><img src="../../assets/images/nav_dashboard.png" alt="Dashboard" width="52px" height="52px">
                        </div>
                    </router-link></b-nav-item>
                <b-nav-item><router-link to="/statistic">Statistic</router-link></b-nav-item>
                <b-nav-item>Another Link</b-nav-item>
                <b-nav-item disabled>Disabled</b-nav-item>
            </b-nav> -->
            <p>{{ msg }}</p>
        </div>
        <!-- <nav>
            {{ show() }}
            <div class=".nav-tag"><router-link to="/profile" v-on:click="setAction('profilt')">
                    <img v-if="icActive === 'profile'" src="../../assets/images/nav_profile_active.png" alt="Profile"
                        width="77px" height="77px" />
                    <img v-else src="../../assets/images/nav_profile.png" alt="Profile" width="52px" height="52px" />
                </router-link></div>

            <div class=".nav-tag"><router-link to="/table" v-on:click="setAction('profilt')">
                    <img v-if="icActive === 'table'" src="../../assets/images/nav_table_active.png" alt="Table" width="77px"
                        height="77px" />
                    <img v-else src="../../assets/images/nav_table.png" alt="Table" width="52px" height="52px" />
                </router-link></div>

            <div class=".nav-tag"><router-link to="/statistic" v-on:click="setAction('profilt')">
                    <img v-if="icActive === 'statistic'" src="../../assets/images/nav_statistic_active.png" alt="Statistic"
                        width="77px" height="77px" />
                    <img v-else src="../../assets/images/nav_statistic.png" alt="Statistic" width="52px" height="52px" />
                </router-link></div>

            <div class=".nav-tag"><router-link to="/dashboard" v-on:click="setAction('profilt')">
                    <img v-if="icActive === 'dashboard'" src="../../assets/images/nav_dashboard_active.png" alt="Dashboard"
                        width="77px" height="77px" />
                    <img v-else src="../../assets/images/nav_dashboard.png" alt="Dashboard" width="52px" height="52px" />
                </router-link></div>

        </nav> -->

        <router-view /> 
        <footer>
            <AppFooter />
        </footer>
    </div>
</template>

<script>
// import axios from 'axios';
import AppFooter from '../AppFooter.vue';

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
nav {
    display: flex;
    align-items: center;
    justify-content: right;
    flex-flow: row;
    gap: 20px;
    flex-direction: row-reverse;

    margin: 20px;
    padding-top: 5px;
    padding-right: 70px;
    padding-bottom: 5px;
    padding-left: 70px;

    background-color: #3D5554;

    border-radius: 360px;
    height: auto;
    width: calc(100%-40px);
}

nav div {
    border-radius: 360px;
}

div .nav-tag {
    height: 100%;
    width: 100%;
}

.nav-tag a {
    height: 100%;
    color: #3D5554;
}

/* nav {
    padding: 20px;
}

nav ul {
    list-style: none;
    margin: 0px;
    padding-right: 20px;
    padding-left: 20px;
    overflow: hidden;
    background-color: #3D5554;
    border-radius: 360px;
}

nav li {
    float: right;
}

li a {
    display: block;
    padding: 15px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    color: #c99c33;
}

li a:hover {
    background-color: #1990B2;
    border-radius: 360px;
    width: 72px;
    height: 72px;
} */
</style>