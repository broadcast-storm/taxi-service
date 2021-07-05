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

export default {
    name: 'Main',
    components: { Header },
    data() {
        return {}
    },
    computed: {
        ...mapGetters('profile', ['profileStats']),
    },
    async mounted() {
        await this.PROFILE_REQUEST_FETCHING()
    },
    methods: {
        ...mapActions('profile', [PROFILE_REQUEST_FETCHING]),
    },
}
</script>

<style lang="scss" scoped></style>
