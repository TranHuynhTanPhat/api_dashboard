import Vue from 'vue'
import Vuex from 'vuex'
import User from './User'
import Nav from './Nav';

Vue.use(Vuex);



export const store = new Vuex.Store({
    modules: {
        user: User,
        nav: Nav
    }

})