export const state = () => ({
    data: []
})

export const multations = {
    storeUser: (state, data) => {
        state.data = data;
    }
}