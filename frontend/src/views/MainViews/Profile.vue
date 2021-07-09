<template>
    <div>
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
                <img
                    class="
                        w-20
                        h-20
                        md:w-36 md:h-36
                        p-1
                        bg-yellow-500
                        rounded-full
                    "
                    src="https://images.pexels.com/photos/61100/pexels-photo-61100.jpeg?crop=faces&fit=crop&h=200&w=200&auto=compress&cs=tinysrgb"
                    alt=""
                />
                <div class="title mt-4 md:mt-10 ml-3 font-bold flex flex-col">
                    <div class="name text-lg md:text-2xl">Вася Пупкин</div>
                    <div class="add text-base md:text-xl text-gray-900 mt-4">
                        nikita220800@mail.ru
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

export default {
    name: 'Profile',
    components: {},
    data() {
        return {
            routesList,
            isOpen: true,
        }
    },
    computed: {},

    async mounted() {},

    methods: {},
}
</script>

<style lang="scss" scoped></style>
