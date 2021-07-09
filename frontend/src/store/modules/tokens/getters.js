const getters = {
    isAuthenticated: (state) => state.refreshToken !== null,
    creatingUserStatus: (state) => state.creatingUserStatus,
    tokenStatus: (state) => state.tokenStatus,
}

export default getters
