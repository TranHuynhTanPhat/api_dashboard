<template>
    <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
    <div>
        <div class="navcontain">
            <div class="letter">{{ msgLogin }}</div>
        </div>
        <div class="contain">
            <form>
                <div><img src="../../../assets/images/admin01.png" alt="Login" width="100px" height="100px"></div>
                <input type="text" v-model="email" placeholder="Enter Email" required />
                <input type="password" v-model="password" placeholder="Enter Password" required />
                <button @click="login({ email, password })" style="background: #1990B2;">Sign in</button>
                <div class="text-contain">
                    <div class="forgotpassword"><router-link to="/auth/forgotpassword">Forgot password?</router-link></div>
                    <div class="donthavaaccount">Don't have account? <router-link to="/auth/register">
                            <div
                                style="font-weight: 500;font-size: 14px;line-height: 16px;display: flex;align-items: center;">
                                Sign up</div>
                        </router-link>
                    </div>
                </div>
            </form>

        </div>

    </div>
</template>
<script>
import axios from 'axios'

const REGISTER = "http://127.0.0.1:8000/user/register"

export default ({
    name: 'LoginPage',

    data() {
        return {
            msgLogin: 'Log in into API DASHBOARD',
            email: '',
            password: '',

        }
    },
    computed: {
        // id: {
        //     get() {
        //         return this.$store.getters['getId']
        //     },
        //     set(value) {
        //         this.$store.ommit('storeId', value)
        //     }
        // },
        // email: {
        //     get() {
        //         return this.$store.getters['getEmail']
        //     },
        //     set(value) {
        //         this.$store.commit('storeEmail', value)
        //     }
        // },
        // password: {
        //     get() {
        //         return this.$store.getters['getPassword']
        //     },
        //     set(value) {
        //         this.$store.commit('storePassword', value)
        //     }
        // },
        // status: {
        //     get() {
        //         return this.$store.getters['getStatus']
        //     },
        //     set(value) {
        //         this.$store.commit('storeStatus', value)
        //     }
        // },
        // role: {
        //     get() {
        //         return this.$store.getters['getRole']
        //     },
        //     set(value) {
        //         this.$store.commit("storeRole", value)
        //     }
        // }
    },
    methods: {
        async login(user) {
            await axios.post(REGISTER, user)
                .then(res => {
                    console.log(res.data)
                })
                .catch(ex => {
                    console.log(ex)
                })
        },

        // async signIn() {
        //     localStorage.removeItem("user-info")
        //     localStorage.setItem("user-info", JSON.stringify(this.email))
        //     this.$router.push({ name: 'Dashboard' }).catch(() => {

        //     })
        // }
    },
    created() {
        localStorage.removeItem("user-info")
    }
})
</script>
<style scoped>
@import '../../../assets/css/form-style.css';
</style>

