<template>
    <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
    <div>
        <div class="navcontain">
            <div class="header-name-page">{{ msgForgotPassword }}</div>
        </div>
        <div class="contain">
            <form @submit.prevent="handlerVerify" v-if="activeOTP == 'send'">
                <input type="email" v-model="email" placeholder="Enter Email" required />
                <button class="login">Send OTP</button>
            </form>
            <form @submit.prevent="handlerVerify" v-if="activeOTP == 'verify'">
                <input v-model="OTP"
                    oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
                    type="number" maxlength="6" required />
                <button class="login">Verify</button>
            </form>
            <form @submit.prevent="handlerVerify" v-if="activeOTP == 'change'"><input v-model="password" type="text"
                    required />
                <button class="login">Change Password</button>
            </form>
        </div>

    </div>
</template>
<script>
// import axios from "axios"

export default ({
    name: 'ForgotPassword',

    data() {
        return {
            msgForgotPassword: 'Forgot password',
            email: "",
            OTP: "",
            password: "",
            activeOTP: "send",
        }
    },
    methods: {
        async handlerVerify() {
            if (this.activeOTP == "send") {
                this.activeOTP = "verify"
                // await axios.get()
            }
            else if (this.activeOTP == "verify") {
                this.activeOTP = "change"
                // await axios.get()
            }
            else {
                this.activeOTP = "send"
                console.log(this.password)
                // await axios.put()

                this.$router.push({ name: 'Signin' })
            }

        },

    }
})
</script>
<style>
@import '../../../assets/css/form-style.css';

form .otp {
    display: flex;
    flex-flow: row;
    justify-items: center;
    align-items: center;
    gap: 20px;

}
</style>

