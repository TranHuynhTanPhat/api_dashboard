export default {
    namespace: true,
    state: {
        labels:[],
        values:[],
    },
    mutations: {

        labels: (state, data) => {
            state.labels = data
        },
        values: (state, data) => {
            state.values = data
        },
        
    },
    getters: {
        getLabels(state) {
            return state.labels
        },
        getValues(state) {
            return state.values
        },
    },
    actions: {
        values(context, data) {
            context.commit('values', data)
        },
        labels(context, data) {
            context.commit('labels', data)
        },}
}