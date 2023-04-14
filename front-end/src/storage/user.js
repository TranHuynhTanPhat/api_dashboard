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
        }
    },
    actions:{
        user(context, data){
            context.commit('user', data)
        }
    }
}