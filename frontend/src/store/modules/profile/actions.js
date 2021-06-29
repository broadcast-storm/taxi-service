import axios from 'axios'
import {
    PROFILE_REQUEST_FETCHING,
    PROFILE_REQUEST_SUCCESS,
    PROFILE_REQUEST_ERROR,
    PROFILE_UPDATE,
    PROFILE_UPDATE_SUCCESS,
    PROFILE_UPDATE_ERROR,
} from '@/store/action-types/profile'
import jwt from 'jsonwebtoken'

const actions = {
    [PROFILE_REQUEST_FETCHING]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            if (token === null) return commit(PROFILE_REQUEST_ERROR, {})
            const userId = jwt.decode(token).user_id
            commit(PROFILE_REQUEST_FETCHING)
            const response = await axios.get(`/api/users/${userId}`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log(response.data)
            commit(PROFILE_REQUEST_SUCCESS, {
                newProfileInfo: response.data,
            })
        } catch (error) {
            commit(PROFILE_REQUEST_ERROR, error)
            throw error
        }
    },
    [PROFILE_UPDATE]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            if (token === null) return commit(PROFILE_REQUEST_ERROR, {})
            const userId = jwt.decode(token).user_id
            commit(PROFILE_UPDATE)
            const response = await axios.get(`/api/users/${userId}`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log(response.data)
            commit(PROFILE_UPDATE_SUCCESS, {
                newProfileInfo: response.data,
            })
        } catch (error) {
            commit(PROFILE_UPDATE_ERROR, error)
            throw error
        }
    },
}

export default actions
