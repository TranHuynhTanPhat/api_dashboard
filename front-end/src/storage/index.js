import Vue from 'vue'
import Vuex from 'vuex'
import user from './user'

Vue.use(Vuex);

// const User = {
//     state: () => ({
//         id: "",
//         email: "",
//         password: "",
//         status: 0,
//         role: 0
//     }),
//     mutations: {
//         storeId: (state, data) => {
//             state.id = data
//         },
//         storeEmail: (state, data) => {
//             state.email = data
//         },
//         storePassword: (state, data) => {
//             state.password = data
//         },
//         storeStatus: (state, data) => {
//             state.status = data
//         },
//         storeRole: (state, data) => {
//             state.role = data
//         },
//     },
//     getters: {
//         getId(state) {
//             return state.id
//         },
//         getEmail(state) {
//             return state.email
//         },
//         getPassword(state) {
//             return state.password
//         },
//         getStatus(state) {
//             return state.status
//         },
//         getRole(state) {
//             return state.role
//         },
//     }
// }

export const store = new Vuex.Store({
    modules: {
        user: user,
    }
})