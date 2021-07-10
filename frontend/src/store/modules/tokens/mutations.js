import {
    AUTH_REQUEST,
    AUTH_REFRESH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_REFRESH_SUCCESS,
    AUTH_LOGOUT,
    AUTH_REFRESH_ERROR,
    FIRST_AUTH_REQUEST_SUCCESS,
    CREATE_USER_REQUEST,
    CREATE_USER_SUCCESS,
    CREATE_USER_ERROR,
    QUIET_REFRESH_REQUEST,
} from '@/store/action-types/tokens'

const mutations = {
    [AUTH_REQUEST]: (state) => {
        state.tokenStatus = 'loading'
    },
    [CREATE_USER_REQUEST]: (state) => {
        state.creatingUserStatus = 'loading'
    },
    [CREATE_USER_SUCCESS]: (state) => {
        state.creatingUserStatus = 'success'
    },
    [CREATE_USER_ERROR]: (state) => {
        state.creatingUserStatus = 'error'
    },
    [FIRST_AUTH_REQUEST_SUCCESS]: (state) => {
        state.firstRequestSuccess = true
    },
    [AUTH_REFRESH_REQUEST]: (state) => {
        state.tokenStatus = 'refreshing'
    },
    [AUTH_SUCCESS]: (state, { accessToken, refreshToken }) => {
        state.tokenStatus = 'success'
        state.accessToken = accessToken
        state.refreshToken = refreshToken
    },
    [AUTH_REFRESH_SUCCESS]: (state, { accessToken }) => {
        state.tokenStatus = 'success'
        state.accessToken = accessToken
    },
    [QUIET_REFRESH_REQUEST]: (state, { accessToken }) => {
        state.accessToken = accessToken
    },
    [AUTH_ERROR]: (state) => {
        state.tokenStatus = 'error'
    },
    [AUTH_REFRESH_ERROR]: (state) => {
        state.tokenStatus = 'error'
        state.accessToken = null
        state.refreshToken = null
        state.firstRequestSuccess = false
    },
    [AUTH_LOGOUT]: (state) => {
        state.tokenStatus = ''
        state.accessToken = null
        state.refreshToken = null
        state.firstRequestSuccess = false
    },
}

export default mutations
