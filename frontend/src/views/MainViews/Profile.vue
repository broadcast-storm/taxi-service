<template>
    <div
        v-if="profileStatus === 'loading'"
        class="h-full flex justify-center items-center"
    >
        <Spinner />
    </div>
    <div v-if="profileStatus === 'success'">
        <div
            class="
                card
                w-full
                relative
                flex flex-col
                mx-auto
                shadow-lg
                h-40
                md:h-56
                m-5
                rounded
                overflow-hidden
            "
        >
            <div class="h-16 md:h-24 w-full absolute top-0 bg-gray-900 z-10" />
            <div class="profile w-full flex m-3 ml-4 text-white z-20">
                <div
                    class="
                        w-20
                        h-20
                        md:w-36 md:h-36
                        p-4
                        bg-yellow-500
                        text-gray-900
                        rounded-full
                    "
                >
                    <svg
                        class="h-full fill-current"
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 350 350"
                    >
                        <g>
                            <path
                                d="M175,171.173c38.914,0,70.463-38.318,70.463-85.586C245.463,38.318,235.105,0,175,0s-70.465,38.318-70.465,85.587
		C104.535,132.855,136.084,171.173,175,171.173z"
                            />
                            <path
                                d="M41.909,301.853C41.897,298.971,41.885,301.041,41.909,301.853L41.909,301.853z"
                            />
                            <path
                                d="M308.085,304.104C308.123,303.315,308.098,298.63,308.085,304.104L308.085,304.104z"
                            />
                            <path
                                d="M307.935,298.397c-1.305-82.342-12.059-105.805-94.352-120.657c0,0-11.584,14.761-38.584,14.761
		s-38.586-14.761-38.586-14.761c-81.395,14.69-92.803,37.805-94.303,117.982c-0.123,6.547-0.18,6.891-0.202,6.131
		c0.005,1.424,0.011,4.058,0.011,8.651c0,0,19.592,39.496,133.08,39.496c113.486,0,133.08-39.496,133.08-39.496
		c0-2.951,0.002-5.003,0.005-6.399C308.062,304.575,308.018,303.664,307.935,298.397z"
                            />
                        </g>
                    </svg>
                </div>
                <div class="title mt-4 md:mt-10 ml-3 font-bold flex flex-col">
                    <div class="name text-lg md:text-2xl">
                        {{ profileInfo.name + ' ' + profileInfo.surname }}
                    </div>
                    <div class="add text-base md:text-xl text-gray-900 mt-4">
                        {{ profileInfo.email }}
                    </div>
                </div>
            </div>
            <div class="flex cursor-pointer space-x-1 mx-auto">
                <router-link
                    :to="
                        routesList.mainPage.children.profilePage.children
                            .editUser.path
                    "
                    class="py-2 px-6 bg-yellow-500 text-gray-900 rounded-md"
                >
                    Инфо
                </router-link>
                <router-link
                    :to="
                        routesList.mainPage.children.profilePage.children
                            .orderCar.path
                    "
                    class="py-2 px-6 bg-gray-900 text-yellow-500 rounded-md"
                >
                    Заказ такси
                </router-link>
            </div>
        </div>
        <div class="w-full lg:w-9/12 mx-auto">
            <router-view />
        </div>
    </div>
</template>

<script>
import routesList from '@/router/routesList'
import { mapGetters } from 'vuex'
import Spinner from '@/components/Spinner'

export default {
    name: 'Profile',
    components: { Spinner },
    data() {
        return {
            routesList,
            isOpen: true,
        }
    },
    computed: {
        ...mapGetters('profile', ['profileStatus', 'profileInfo']),
    },

    async mounted() {},

    methods: {},
}
</script>

<style lang="scss" scoped></style>
