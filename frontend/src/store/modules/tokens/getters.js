const getters = {
    isAuthenticated: (state) => state.refreshToken !== null,
    creatingUserStatus: (state) => state.creatingUserStatus,
    getAccessToken: (state) => state.accessToken,
    tokenStatus: (state) => state.tokenStatus,
    firstRequestSuccess: (state) => state.firstRequestSuccess,
}

export default getters
