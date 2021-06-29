const getters = {
    isAuthenticated: (state) => state.refreshToken !== null,
    creatingUserStatus: (state) => state.creatingUserStatus,
}

export default getters
