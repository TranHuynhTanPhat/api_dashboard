export default {
    namespace: true,
    state: {
        isProfile: false,
        isDashboard: false,
        isStatistic: false,
        isTable: false,
        isSetting: false
    },
    mutations: {

        isProfile: (state) => {
            state.isProfile = true
            state.isDashboard = false
            state.isStatistic = false
            state.isSetting = false
            state.isTable = false
        },
        isDashboard: (state) => {
            state.isDashboard = true
            state.isProfile = false
            state.isStatistic = false
            state.isTable = false
            state.isSetting = false
        },
        isStatistic: (state) => {
            state.isStatistic = true
            state.isDashboard = false
            state.isProfile = false
            state.isTable = false
            state.isSetting = false
        },
        isTable: (state) => {
            state.isTable = true
            state.isDashboard = false
            state.isProfile = false
            state.isStatistic = false
            state.isSetting = false
        },
        isDisable: (state) => {
            state.isTable = false
            state.isDashboard = false
            state.isProfile = false
            state.isStatistic = false
            state.isSetting = false
        },
        isSetting: (state) => {
            state.isTable = false
            state.isDashboard = false
            state.isProfile = false
            state.isStatistic = false
            state.isSetting = true
        }
    },
    getters: {
        getIsProfile(state) {
            return state.isProfile
        }
    },
    actions: {
        async isProfile(context) {
            context.commit('isProfile')
        },
        isDashboard(context) {
            context.commit('isDashboard')
        },
        isStatistic(context) {
            context.commit('isStatistic')
        },
        isTable(context) {
            context.commit('isTable')
        },
        isSetting(context) {
            context.commit('isSetting')
        }
        // stateFalse(context, data) {
        //     context.commit('storeStateFalse', data)
        // }
    }
}