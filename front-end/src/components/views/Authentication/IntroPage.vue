<template>
    <div>
        <header>
            <nav>
                <ul>
                    <li><router-link to="/auth/register" class="important" target="_parent">{{ msgSignUp }}</router-link>
                    </li>
                    <li><router-link to="/auth/login" target="_parent">{{ msgSignIn }}</router-link></li>
                </ul>
            </nav>
        </header>
        <div class="intro">
            <img src="../../../assets/images/intro.png" width="80%" />
        </div>
    </div>
</template>
<script scoped>
export default {
    name: "IntroPage",
    data: () => ({
        msgSignUp: 'Sign up',
        msgSignIn: 'Login'
    }),
    components: {
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
    color:#c99c33;
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

.intro {
    position: relative;
    margin-left: 0%;
    margin-top: 10%;
    margin-bottom: 10%;
}
</style>