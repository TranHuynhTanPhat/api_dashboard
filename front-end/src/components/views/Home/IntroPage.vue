<template>
    <div>
        <nav v-if="activeNav === 'logout'">
            <ul>
                <li><router-link to="/auth/register" class="important" target="_parent">{{ msgSignUp }}</router-link>
                </li>
                <li><router-link to="/auth/login" target="_parent">{{ msgSignIn }}</router-link></li>
            </ul>
        </nav>
        <nav v-else>
            <ul>
                <li>
                    <div @click.prevent="handlerClick" class="important" target="_parent">{{ msgLogout
                    }}</div>
                </li>
                <li><router-link to="/dashboard" target="_parent">{{ msgHome }}</router-link></li>
            </ul>
        </nav>
        <div class="intro">
            <img src="../../../assets/images/intro.png" width="80%" />
        </div>
        <AppFooter />

    </div>
</template>
<script scoped>
import AppFooter from '@/components/AppFooter.vue';
export default {
    name: "IntroPage",
    data: () => ({
        msgHome: 'Home',
        msgSignUp: 'Sign up',
        msgSignIn: 'Login',
        msgLogout: 'Logout',
        activeNav: 'logout'
    }),
    components: {
        AppFooter,
    },
    methods: {
        async handlerClick() {
            localStorage.removeItem('token')
            localStorage.removeItem('id')
            localStorage.removeItem('email')
            localStorage.removeItem('status')
            localStorage.removeItem('role')
            this.$router.go()

        }
    },
    mounted() {
        if (localStorage.getItem('id') != null || localStorage.getItem('token') != null) {
            this.activeNav = "login"
        } else {
            this.activeNav = "logout"
        }
    }
};
</script>
<style scoped>
nav {
    padding: 20px;
}

nav ul {
    list-style: none;
    margin: 0px;
    padding: 0px;
    overflow: hidden;
    background-color: transparent;
}

nav li {
    float: right;
}

li a {
    display: block;
    padding: 10px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    color: #c99c33;
}

a.important {
    border-style: solid;
    border-radius: 10px;
}

li a:hover {
    color: #c99c337c;
}

li a.important:hover {
    background-color: #c99c33;
    color: white;
}

li div {
    display: block;
    padding: 10px;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    color: #c99c33;
    cursor: pointer;
}

div.important {
    border-style: solid;
    border-radius: 10px;
}

li div:hover {
    color: #c99c337c;
}

li div.important:hover {
    background-color: #c99c33;
    color: white;
}

.intro {
    position: relative;
    margin-left: 0%;
}
</style>