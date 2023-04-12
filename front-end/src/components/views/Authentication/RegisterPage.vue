<template>
    <div>
        <div class="navcontain">
            <div class="letter">{{ msgSignUp }}</div>
        </div>
        <div class="contain">
            <form>
                <div><img src="../../../assets/images/add01.png" alt="Login" width="100px" height="100px"></div>
                <input type="text" v-model="email" placeholder="Enter Email" name="email" />
                <div class="pass-contain">
                    <input type="password" v-model="password" placeholder="Enter Password" name="password" />
                    <input type="password" v-model="confirm_password" placeholder="Enter Confirm Password"
                        name="confirm_password" />
                </div>
                <button @click="register({ email, password })">Register</button>
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
        async register(user) {
            await axios.post(REGISTER, user)
                .then(res => {
                    console.log("RegisterPage: " + res.data)
                    if (res.status == "success") {
                        this.$router.push('/auth/login')
                    }
                })
                .catch(ex => {
                    console.log(ex)
                })
        }
    }
}
</script>
<style scoped>
@import '../../../assets/css/form-style.css';
</style>