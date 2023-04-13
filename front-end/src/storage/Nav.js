export default {
    namespace: true,
    state: {
        active: "anonymous"
    },
    mutations: {
        storeActive: (state, data) => {
            state.active = data
        }
    },
    getters: {

        getActive(state) {
            return state.active
        }
    },
    actions: {
        user(context, data) {
            context.commit('storeActive', data)
        }
    }
}