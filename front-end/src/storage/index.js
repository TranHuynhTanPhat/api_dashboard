import Vue from 'vue'
import Vuex from 'vuex'
import Nav from './Nav';

Vue.use(Vuex);



export const store = new Vuex.Store({
    modules: {
        nav: Nav
    }

})