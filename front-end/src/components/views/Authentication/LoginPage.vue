<template>
    <!-- <div class="bg-btn-login"><div class="letter-btn-login">{{ msgLogin }}</div></div> -->
    <div>
        <div class="navcontain">
            <div class="letter">{{ msgLogin }}</div>
        </div>
        <div class="contain">
            <div class="form">
                <div><img src="../../../assets/images/admin01.png" alt="Login" width="100px" height="100px"></div>
                <input type="text" v-model="email" placeholder="Enter Email" />
                <input type="text" v-model="password" placeholder="Enter Password" name="password" />
                <button @click="signIn">Sign in</button>
                <div class="contain">
                    <div class="forgotpassword"><router-link to="/auth/forgotpassword">Forgot password?</router-link></div>
                    <div class="donthavaaccount">Don't have account? <router-link to="/auth/register">
                            <div
                                style="font-weight: 500;font-size: 14px;line-height: 16px;display: flex;align-items: center;">
                                Sign up</div>
                        </router-link>
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>
<script>
import axios from 'axios'

const REGISTER = "http://127.0.0.1:8000/register"
// import { user, setUser } from "../../../store/User"

export default ({
    name: 'LoginPage',

    data() {
        return {
            msgLogin: 'Log in into API DASHBOARD'
        }
    },
    computed: {
        // id: {
        //     get() {
        //         return user.id
        //     },
        //     set(value) {
        //         setUser.storeId("user/storeId", value)
        //     }
        // },
        // email: {
        //     get() {
        //         return user.email
        //     },
        //     set(value) {
        //         setUser.storeEmail("user/storeEmai", value)
        //     }
        // },
        // password: {
        //     get() {
        //         return user.password
        //     },
        //     set(value) {
        //         this.$store.commit("user/storePassword", value)
        //     }
        // },
        // status: {
        //     get() {
        //         return this.$store.state.user.status
        //     },
        //     set(value) {
        //         this.$store.commit("user/storeStatus", value)
        //     }
        // },
        // role: {
        //     get() {
        //         return this.$store.state.user.role
        //     },
        //     set(value) {
        //         this.$store.commit("user/storeRole", value)
        //     }
        // }
    },
    methods: {
        async login(user) {
            await axios.post(REGISTER, user)
                .then(res => {
                    console.log(res.data)
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

.form input[type=text] {

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

.form input[type=text]::placeholder {
    color: #3D555466;
}

.form input[type=text]:focus {
    border-style: solid;
    border-width: 3px;
    border-color: #3d55547d;
}

.form button {
    width: 30%;
    height: 45px;

    /* 1990B2 */

    background: #1990B2;
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

