const state = {
    accessToken: null,
    refreshToken: localStorage.getItem('refresh_token') || null,
    tokenStatus: '',
    firstRequestSuccess: false,
    creatingUserStatus: null,
}

export default state
