<template>
    <div>
        <div class="navcontain">
            <div class="letter">{{ msgSignUp }}</div>
        </div>
        <div class="contain">
            <div class="form">
                <div><img src="../../../assets/images/add01.png" alt="Login" width="100px" height="100px"></div>
                <input type="text" v-model="email" placeholder="Enter Email" name="email" />
                <input type="password" v-model="password" placeholder="Enter Password" name="password" />
                <input type="password" v-model="confirm_password" placeholder="Enter Confirm Password"
                    name="confirm_password" />
                <button @click="register({email, password })">Register</button>
                <div class="contain">
                    <div class="donthavaaccount">Already have account? <router-link to="/auth/login">
                            <div
                                style="font-weight: 500;font-size: 14px;line-height: 16px;display: flex;align-items: center;color:#1990B2">
                                Login</div>
                        </router-link>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
<script>
import axios from 'axios'

const REGISTER = "http://127.0.0.1:8000/user/register"


export default {
    name: 'RegisterPage',
    data() {
        return {
            msgSignUp: 'Register API Dashboard account',
            email: "",
            password:"",
            confirm_password:""
        }
    },
    methods: {
        async register(user) {
            await axios.post(REGISTER, user)
                .then(res => {
                    console.log(res.data)
                })
                .catch(ex => {
                    console.log(ex)
                })
        }
    }
}
</script>
<style scoped>
.navcontain {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 10px;
    height: 60px;
    padding: 20px;

    margin-top: 20px;
}

.letter {
    width: 100%;
    height: 60px;
    font-family: 'Roboto';
    font-style: normal;
    font-weight: 900;
    font-size: 36px;
    line-height: 60px;
    display: flex;
    align-items: center;
    flex-flow: column;
    color: #C99C33;
    background: url('../../../assets/images/navbar.png'), #3D5554;
    border-radius: 360px;
}

.contain {
    display: flex;
    flex-direction: columns;
    justify-content: center;
    align-items: center;
}

.form {
    /* Auto layout */

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 50px;
    gap: 20px;

    position: relative;
    height: 510px;
    width: 700px;

    margin-top: 100px;
    margin-bottom: 100px;


    background: url('../../../assets/images/form.png'), #FFFFFF;
    background-position: center;
    background-repeat: no-repeat;
    background-size: contain;
    box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.25);
    border-radius: 25px;


}

.form input {

    font-weight: 600;
    font-size: 24px;
    color: #3D5554;

    width: 100%;
    height: 60px;

    padding-left: 20px;
    padding-right: 20px;

    background: #F3F3F3;
    border-radius: 30px;
    outline: none;
}

.form input::placeholder {
    color: #3D555466;
}

.form input:focus {
    border-style: solid;
    border-width: 3px;
    border-color: #3d55547d;
}

.form button {
    width: 30%;
    height: 45px;

    /* 1990B2 */

    background: #C99C33;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.25);
    border-radius: 25px;
    font-weight: 700;
    font-size: 20px;
    line-height: 45px;
    color: #FFFFFF;
}

.form .contain {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 5px;
    width: 100%;
    height: 30px;
}
.form .contain .forgotpassword a {
    font-weight: 400;
    font-size: 12px;
    line-height: 14px;
    color: #3D5554;
    text-decoration: none;
}

.form .contain .donthavaaccount {
    font-weight: 400;
    font-size: 14px;
    line-height: 16px;
    display: flex;
    align-items: center;
    color: #3D5554;
}

.donthavaaccount a {
    padding-left: 10px;
    text-decoration: none;
}
</style>