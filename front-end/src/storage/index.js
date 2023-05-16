import Vue from 'vue'
import Vuex from 'vuex'
import Nav from './Nav';
import ChartDashboard from './ChartDashboard';
import HODashboard from './HODashboard';

Vue.use(Vuex);



export const store = new Vuex.Store({
    modules: {
        nav: Nav,
        chartDashboard: ChartDashboard,
        hoDashboard: HODashboard
    }

})