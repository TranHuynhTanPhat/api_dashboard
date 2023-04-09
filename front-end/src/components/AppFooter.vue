<template>
    <footer>
        <div class="containlogo"><a href="/intro" target="_parent"><img src="../assets/images/logo.png" alt="Logo Website"
                    height="117px" width="130px" /></a>
            <span>API is the product of the course project</span>
        </div>
        <div class="contain">
            <span class="title">Useful link</span>
            <div class="content">
                <span><a href="#">Home</a></span>
                <span><a href="#">Statistic</a></span>
                <span><a href="#">Data table</a></span>
                <span><a class="important" href="#">Sign up now</a></span>
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
    }
}
</script>
<style scoped>
footer {
    /* footer */


    /* Auto layout */

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    padding: 192px 120px 72px;
    gap: 50px;

    width: 100%;
    height: auto;

    /* E1ECEB */

    background-color: #e1eceb;

    /* Inside auto layout */

    flex-wrap: wrap;
    order: 1;
    align-self: stretch;
    flex-grow: 0;

    clear: both;
    position: relative;
    overflow: hidden;
}

.containlogo {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    padding: 10px;
    gap: 10px;

    width: 257.5px;
    height: 169px;


    /* Inside auto layout */

    flex: none;
    order: 0;
    align-self: stretch;
    flex-grow: 1;
}

.containlogo span {
    font-weight: 900;
    color: #3d5554;
    font-size: 14px;
    font-style: italic;
}

.contain {
    /* Auto layout */

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: left;
    padding: 10px;
    gap: 10px;

    width: auto;
    height: 100%;


    /* Inside auto layout */

    flex: none;
    order: 0;
    align-self: stretch;
    flex-grow: 1;
}

span.title {
    font-size: 24px;
    color: #3d5554;
    font-weight: 700;
}

.contain div.content {
    /* Auto layout */

    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0px;
    gap: 5px;

    width: auto;
    height: 100%;


    /* Inside auto layout */

    flex: none;
    order: 1;
    align-self: stretch;
    flex-grow: 0;

}

.content span {
    color: #3d5554;
    font-size: 14px;
}

.content a {
    display: contents;
    text-decoration: none;

    color: #3d5554;
    font-size: 14px;
}

.content a.important {
    font-weight: 900;
}

.content a:hover {
    color: #c99c33;
}

.contain div.contact {
    /* Auto layout */

    display: flex;
    flex-direction: row;
    align-items: left;
    padding: 0px;
    gap: 10px;

    width: auto;
    height: 100%;


    /* Inside auto layout */

    flex: none;
    order: 1;
    flex-grow: 0;
}
</style>