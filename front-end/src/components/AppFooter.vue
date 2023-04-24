<template>
    <footer>
        <div class="containlogo"><a href="/" target="_parent"><img src="../assets/images/logo.png" alt="Logo Website"
                    height="117px" width="130px" /></a>
            <span>API is the product of the course project</span>
        </div>
        <div class="contain">
            <span class="title">Useful link</span>
            <div class="content">
                <span><a href="/dashboard">Home</a></span>
                <span><a href="/statistic">Statistic</a></span>
                <span><a href="/table">Data table</a></span>
                <span><div class="important" @click.prevent="handleSendToSignUp">Sign up now</div></span>
            </div>
        </div>
        <div class="contain">
            <span class="title">Follow us</span>
            <div class="contract">
                <a href="https://facebook.com">
                    <img src="../assets/images/App05.png" alt="Facebook" width="30px" height="30px" /></a>
                <a href="https://twitter.com">
                    <img src="../assets/images/App04.png" alt="Twitter" width="30px" height="30px" /></a>
                <a href="https://instagram.com">
                    <img src="../assets/images/App03.png" alt="Instagram" width="30px" height="30px" /></a>
                <a href="https://wechat.com">
                    <img src="../assets/images/App02.png" alt="Wechat" width="30px" height="30px" /></a>
                <a href="https://youtube.com">
                    <img src="../assets/images/App01.png" alt="Youtube" width="30px" height="30px" /></a>
            </div>
        </div>
        <div class="contain">
            <span class="title">Group 13</span>
            <div class="content">
                <span>Trần Huỳnh Tấn Phát</span>
                <span>Mai Hải Đăng</span>
                <span>Võ Văn Nghĩa</span>
            </div>
        </div>
    </footer>
</template>
<script scoped>
export default {
    name: 'AppFooter',
    data() {
        return {

        }
    },
    methods:{
        handleSendToSignUp(){
            this.$router.push({name:"Signup"})
        }
    }
}
</script>
<style scoped>
@import '../assets/css/footer-style.css';
</style>