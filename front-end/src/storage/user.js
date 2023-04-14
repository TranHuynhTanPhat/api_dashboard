export default {
    namespace: true,
    state: {
        user:{

        }
    },
    mutations: {
        user: (state, data) => {
            state.user = data
        }
    },
    getters: {
        getUser(state){
            return state.user
        },
        getEmail(state){
            return state.user['email']
        }
    },
    actions:{
        user(context, data){
            context.commit('storeUser', data)
        }
    }
}