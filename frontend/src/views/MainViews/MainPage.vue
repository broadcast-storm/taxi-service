<template>
    <div class="">
        <div class="header rounded overflow-hidden relative">
            <div
                class="
                    h-full
                    flex flex-col
                    items-start
                    justify-between
                    bg-black bg-opacity-60
                    py-6
                    px-6
                    sm:px-4 sm:py-12
                    lg:px-8
                "
            >
                <span class="text-white text-4xl md:text-6xl font-bold mb-4"
                    >Нет времени ждать?</span
                >

                <a
                    href="tel:5554280940"
                    class="
                        group
                        relative
                        w-full
                        max-w-md
                        flex
                        justify-center
                        py-2
                        sm:py-3 sm:my-3
                        my-2
                        px-4
                        border border-transparent
                        text-base
                        font-medium
                        rounded-md
                        text-white
                        bg-yellow-500
                        hover:bg-yellow-600
                        focus:outline-none
                        focus:ring-2
                        focus:ring-offset-2
                        focus:ring-white
                    "
                    >Заказать по телефону</a
                >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'MainPage',
    components: {},
    computed: {},

    async mounted() {},

    methods: {},
}
</script>

<style lang="scss" scoped>
.header {
    height: 45vh;
    background-image: url('~@/assets/img/main/header.jpg');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
}
</style>
