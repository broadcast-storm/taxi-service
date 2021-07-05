import axios from 'axios'
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
} from '@/store/action-types/tokens'

const actions = {
    [CREATE_USER_REQUEST]: async ({ commit }, userCredentials) => {
        try {
            commit(CREATE_USER_REQUEST)
            const response = await axios.post(
                '/api/login',
                {
                    email: userCredentials.username,
                    name: userCredentials.password,
                    surname: userCredentials.password,
                    password: userCredentials.password,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            commit(AUTH_SUCCESS, {
                accessToken: response.data.access,
                refreshToken: response.data.refresh,
            })
            commit(CREATE_USER_SUCCESS)
            localStorage.setItem('refresh_token', response.data.refresh)
        } catch (error) {
            commit(CREATE_USER_ERROR, error)
            throw error
        }
    },
    [AUTH_REQUEST]: async ({ commit }, userCredentials) => {
        try {
            commit(AUTH_REQUEST)
            const response = await axios.post(
                '/api/login',
                {
                    username: userCredentials.email,
                    password: userCredentials.password,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            commit(AUTH_SUCCESS, {
                accessToken: response.data.access,
                refreshToken: response.data.refresh,
            })
            commit(FIRST_AUTH_REQUEST_SUCCESS)
            localStorage.setItem('refresh_token', response.data.refresh)
        } catch (error) {
            commit(AUTH_ERROR, error)
            throw error
        }
    },
    [AUTH_REFRESH_REQUEST]: async ({ commit, state }) => {
        try {
            commit(AUTH_REFRESH_REQUEST)
            const response = await axios.post(
                '/api/refresh-token',
                {
                    refresh: state.refreshToken,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            commit(AUTH_REFRESH_SUCCESS, {
                accessToken: response.data.access,
            })

            if (!state.firstRequestSuccess) commit(FIRST_AUTH_REQUEST_SUCCESS)
        } catch (error) {
            commit(AUTH_REFRESH_ERROR)
            localStorage.removeItem('refresh_token')
            throw error
        }
    },
    [AUTH_LOGOUT]: async ({ commit, state }) => {
        try {
            await axios.post(
                '/api/logout',
                {
                    refresh_token: state.refreshToken,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            commit(AUTH_LOGOUT)
            localStorage.removeItem('refresh_token')
        } catch (error) {
            commit(AUTH_ERROR)
            throw error
        }
    },
}

export default actions