<template>
    <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
    <div>
        <div class="navcontain">
            <div class="header">{{ msgLogin }}</div>
        </div>
        <div class="contain">
            <form @submit.prevent="handlerSubmit">
                <div><img src="../../../assets/images/admin01.png" alt="Login" width="100px" height="100px"></div>
                <input type="text" v-model="email" placeholder="Enter Email" required />
                <input type="password" v-model="password" placeholder="Enter Password" required />
                <button>Sign in</button>
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
import { LOGIN } from '@/axios'


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

    },
    methods: {
        async handlerSubmit() {
            await axios.post(LOGIN, { "email": this.email, "password": this.password })
                .then(res => {
                    if (res.status == 200) {
                        this.$store.commit('user', res.data.data)
                        localStorage.setItem('token', res.data.token)
                        console.log(this.$store.state.user)
                        console.log(localStorage.getItem('token'))


                        this.$router.push('/dashboard')

                        // console.log((res.data.data ))
                    }
                })
                .catch(ex => {
                    console.log(ex)
                })
        }
    },

    // async signIn() {
    //     localStorage.removeItem("user-info")
    //     localStorage.setItem("user-info", JSON.stringify(this.email))
    //     this.$router.push({ name: 'Dashboard' }).catch(() => {

    //     })
    // }
    // },
    created() {
        localStorage.removeItem('token')
        this.$store.commit('user', null)
    }
})
</script>
<style>
@import '../../../assets/css/form-style.css';

.text-contain .forgotpassword a:hover {
    color: #3d55547a;
}
</style>

