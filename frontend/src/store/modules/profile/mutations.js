import {
    PROFILE_REQUEST_FETCHING,
    PROFILE_REQUEST_SUCCESS,
    PROFILE_REQUEST_ERROR,
    PROFILE_UPDATE,
    PROFILE_UPDATE_SUCCESS,
    PROFILE_UPDATE_ERROR,
} from '@/store/action-types/profile'

const mutations = {
    [PROFILE_REQUEST_FETCHING]: (state) => {
        state.profileStatus = 'loading'
    },
    [PROFILE_REQUEST_SUCCESS]: (state, { newProfileInfo }) => {
        state.profileStatus = 'success'
        state.profileInfo = { ...newProfileInfo }
    },
    [PROFILE_REQUEST_ERROR]: (state) => {
        state.profileStatus = 'error'
    },

    [PROFILE_UPDATE]: (state) => {
        state.profileUpdateStatus = 'loading'
    },
    [PROFILE_UPDATE_SUCCESS]: (state, { newProfileInfo }) => {
        state.profileUpdateStatus = 'success'
        state.profileInfo = { ...newProfileInfo }
    },
    [PROFILE_UPDATE_ERROR]: (state) => {
        state.profileUpdateStatus = 'error'
    },
}

export default mutations
