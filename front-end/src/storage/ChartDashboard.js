export default {
    namespace: true,
    state: {
        count: [],
        stateOk: [],
        stateFail: [],
        angleId: null,
        predicts:[],
        predict_values:[]
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
        },
        predicts: (state, data) => {
            state.predicts = data
        },
        predict_values: (state, data) => {
            state.predict_values = data
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
        },
        getPredicts(state) {
            return state.predicts
        },
        getPredict_values(state) {
            return state.predict_values
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
        },
        predicts(context, data) {
            context.commit('predicts', data)
        },
        predict_values(context, data) {
            context.commit('predict_values', data)
        }
    }
}