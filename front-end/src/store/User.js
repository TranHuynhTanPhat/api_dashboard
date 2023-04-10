export const user = () => ({
    id: "",
    email: "",
    password: "",
    status: 0,
    role: 0
})

export const setUser = {
    storeId: (user, data) => {
        user.id = data;
    },
    storeEmail: (user, data) => {
        user.email = data;
    },
    storePassword: (user, data) => {
        user.password = data;
    },
    storeStatus: (user, data) => {
        user.status = data;
    },
    storeRole: (user, data) => {
        user.Role = data;
    },
}