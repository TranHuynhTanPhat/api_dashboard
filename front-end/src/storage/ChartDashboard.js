export default {
    namespace: true,
    state: {
        count: [],
        stateOk: [],
        stateFail: [],
        angleId: null
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
        angleId: (state, data) => {
            state.angleId = data
        }
    },
    getters: {
        getCount(state) {
            return state.count
        },
        getStateOk(state) {
            return state.stateOk
        },
        getStateFail(state) {
            return state.stateFail
        },
        getAngleId(state) {
            return state.angleId
        }
    },
    actions: {
        count(context, data) {
            context.commit('count', data)
        },
        stateOk(context, data) {
            context.commit('stateOk', data)
        },
        stateFail(context, data) {
            context.commit('stateFail', data)
        },
        angleId(context, data) {
            context.commit('angleId', data)
        }
    }
}