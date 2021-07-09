<template>
    <div class="relative min-h-screen md:flex">
        <Header />
        <div
            class="
                flex-1
                p-2
                pt-16
                space-y-2
                min-h-screen
                md:space-y-8 md:p-8 md:ml-64
                bg-gray-300
            "
        >
            <router-view />
        </div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { PROFILE_REQUEST_FETCHING } from '@/store/action-types/profile'
import Header from '@/components/Header'
import { AUTH_REFRESH_REQUEST } from '@/store/action-types/tokens'

export default {
    name: 'Main',
    components: { Header },
    data() {
        return {}
    },
    computed: {
        ...mapGetters('profile', ['profileStatus']),
        ...mapGetters('tokens', ['tokenStatus', 'isAuthenticated']),
    },

    watch: {
        tokenStatus: async function (val) {
            if (val === 'success') await this.PROFILE_REQUEST_FETCHING()
        },
    },
    async mounted() {
        if (this.isAuthenticated) await this.AUTH_REFRESH_REQUEST()
    },
    methods: {
        ...mapActions('profile', [PROFILE_REQUEST_FETCHING]),
        ...mapActions('tokens', [AUTH_REFRESH_REQUEST]),
    },
}
</script>

<style lang="scss" scoped></style>
