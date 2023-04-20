export default {
    namespace: true,
    state: {
        count:[],
        stateOk:[],
        stateFail:[]
    },
    mutations: {

        count: (state, data) => {
            state.count = data
        },
        stateOk: (state, data) => {
            state.stateOk = data
        },
        stateFail: (state, data) => {
            state.stateFail = data
        },
    },
    getters: {
        getCount(state) {
            return state.count
        },
        getStateOk(state){
            return state.stateOk
        },
        getStateFail(state){
            return state.stateFail
        }
    },
    actions: {
        count(context, data) {
            context.commit('count', data)
        },
        stateOk(context, data){
            context.commit('stateOk', data)
        },
        stateFail(context, data){
            context.commit('stateFail', data)
        }
    }
}