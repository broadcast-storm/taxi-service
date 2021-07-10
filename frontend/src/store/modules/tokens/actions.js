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
    QUIET_REFRESH_REQUEST,
} from '@/store/action-types/tokens'
import { PROFILE_REQUEST_SUCCESS } from '@/store/action-types/profile'

const actions = {
    [CREATE_USER_REQUEST]: async ({ commit }, userCredentials) => {
        try {
            commit(CREATE_USER_REQUEST)
            const response = await axios.post(
                '/api/create-user',
                {
                    user: {
                        email: userCredentials.email,
                        name: userCredentials.name,
                        surname: userCredentials.surname,
                        password: userCredentials.password,
                    },
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )
            console.log(response.data)
            commit(
                `profile/${PROFILE_REQUEST_SUCCESS}`,
                {
                    newProfileInfo: response.data.user,
                },
                { root: true }
            )
            commit(AUTH_SUCCESS, {
                accessToken: response.data.tokens.access,
                refreshToken: response.data.tokens.refresh,
            })
            commit(CREATE_USER_SUCCESS)
            localStorage.setItem('refresh_token', response.data.tokens.refresh)
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
                    user: {
                        email: userCredentials.email,
                        password: userCredentials.password,
                    },
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                }
            )

            console.log(response.data)
            commit(
                `profile/${PROFILE_REQUEST_SUCCESS}`,
                {
                    newProfileInfo: response.data.user,
                },
                { root: true }
            )
            commit(AUTH_SUCCESS, {
                accessToken: response.data.tokens.access,
                refreshToken: response.data.tokens.refresh,
            })
            commit(FIRST_AUTH_REQUEST_SUCCESS)
            localStorage.setItem('refresh_token', response.data.tokens.refresh)
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
    [QUIET_REFRESH_REQUEST]: async ({ commit, state }) => {
        try {
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
            commit(QUIET_REFRESH_REQUEST, {
                accessToken: response.data.access,
            })
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
