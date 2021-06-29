<template>
    <div class="relative min-h-screen md:flex">
        <Header />
        <router-view class="flex-1 p-2 md:p-8 bg-gray-300" />
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
