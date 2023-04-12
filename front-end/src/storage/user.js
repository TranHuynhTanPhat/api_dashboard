export default {
    namespace: true,
    state: {
        id: "",
        email: ""
    },
    mutations: {
        storeId: (state, data) => {
            state.id = data
        },
        storeEmail: (state, data) => {
            state.email = data
        }
    },
    getters: {
        getId(state) {
            return state.id
        },
        getEmail(state) {
            return state.email
        }
    }
}