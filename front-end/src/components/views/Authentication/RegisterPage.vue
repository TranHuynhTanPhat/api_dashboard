<template>
    <div>
        <div class="navcontain">
            <div class="header">{{ msgSignUp }}</div>
        </div>
        <div class="contain">
            <form @submit.prevent="handleSubmit">
                <div><img src="../../../assets/images/add01.png" alt="Login" width="100px" height="100px"></div>
                <input type="email" v-model="email" placeholder="Enter Email" name="email" required />
                <div class="pass-contain">
                    <input type="password" v-model="password" placeholder="Enter Password" name="password" required />
                    <input type="password" v-model="confirm_password" placeholder="Confirm Password" name="confirm_password"
                        required />
                </div>
                <button>Register</button>
                <div class="text-contain">
                    <div class="donthavaaccount">Already have account? <router-link to="/auth/login">
                            <div
                                style="font-weight: 500;font-size: 14px;line-height: 16px;display: flex;align-items: center;color:#1990B2">
                                Login</div>
                        </router-link>
                    </div>
                </div>
            </form>

        </div>
    </div>
</template>
<script>
import axios from 'axios'

import { REGISTER } from '@/axios'


export default {
    name: 'RegisterPage',
    data() {
        return {
            msgSignUp: 'Register API Dashboard account',
            email: "",
            password: "",
            confirm_password: ""
        }
    },
    methods: {
        async handleSubmit() {
            await axios.post(REGISTER, { "email": this.email, "password": this.password })
                .then(res => {
                    if (res.status == 200) {
                        this.$router.push({ name: "Signin" })
                    }
                })
                .catch(ex => {
                    console.log(ex)
                })
        }
    }
}
</script>
<style>
@import '../../../assets/css/form-style.css';
</style>