export default {
    namespace: true,
    state: {
        // id: "",
        // email: "",
        // status: 0,
        // role: 1,
        // // token: ""
        user:{

        }
    },
    mutations: {
        // storeId: (state, data) => {
        //     state.id = data
        // },
        // storeEmail: (state, data) => {
        //     state.email = data
        // },
        // storeStatus: (state, data) => {
        //     state.status = data
        // },
        // storeRole: (state, data) => {
        //     state.role = data
        // },
        // storeToken: (state, data) => {
        //     state.token = data
        // },
        storeUser: (state, data) => {
            // state.id = data.id
            // state.email = data.email
            // state.status = data.status
            // state.role = data.role
            // state.token = data.token
            state.user = data
        }
    },
    getters: {
        // getId(state) {
        //     return state.id
        // },
        // getEmail(state) {
        //     return state.email
        // },
        // getStatus(state) {
        //     return state.status
        // },
        // getRole(state) {
        //     return state.role
        // },
        // getToken(state) {
        //     return state.token
        // },
    },
    actions:{
        user(context, data){
            context.commit('storeUser', data)
        }
    }
}