import Vuex from 'vuex'

import profile from '@/store/modules/profile'
import tokens from '@/store/modules/tokens'

export default new Vuex.Store({
    modules: {
        profile,
        tokens,
    },
})
