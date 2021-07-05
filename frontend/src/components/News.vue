<template>
    <div class="space-y-4 relative">
        <span class="text-4xl font-bold text-yellow-500">Новости</span>
        <div class="flex flex-col lg:flex-row">
            <div
                class="
                    h-48
                    flex
                    relative
                    overflow-hidden
                    justify-center
                    items-center
                    mr-4
                    lg:flex-1
                    bg-gray-300
                    rounded
                "
            >
                <img
                    :src="require('@/assets/img/main/header.jpg')"
                    alt=""
                    class="
                        border-none
                        block
                        w-full
                        h-full
                        absolute
                        object-cover
                        top-0
                        left-0
                    "
                />
            </div>

            <div class="text-left lg:flex-2">
                <h3 class="mb-2 text-white text-2xl font-bold">
                    Очень интересная акция
                </h3>
                <h4 class="mb-2 text-gray-200 text-sm text-yellow-500">
                    Акция
                </h4>
                <p class="text-white text-sm">
                    Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                    Aenean commodo ligula eget dolor. Aenean massa. Cum sociis
                    natoque penatibus et magnis dis parturient montes, nascetur
                    ridiculus mus. Donec quam felis, ultricies nec, pellentesque
                    eu, pretium quis, sem.
                </p>
                <div class="mt-4">
                    <router-link
                        :to="`${routesList.mainPage.children.newsPage.path}/1`"
                        class="
                            no-underline
                            mr-4
                            text-yellow-500
                            hover:text-yellow-600
                            font-bold
                        "
                        >Подробнее...</router-link
                    >
                </div>
            </div>
        </div>
        <router-link
            :to="routesList.mainPage.children.newsPage.path"
            class="
                relative
                w-52
                lg:w-1/3
                max-w-md
                flex
                justify-center
                py-2
                ml-auto
                px-2
                text-base
                font-medium
                rounded-md
                text-white
                bg-yellow-500
                hover:bg-yellow-600
            "
            >Читать все новости...</router-link
        >
    </div>
</template>

<script>
import routesList from '@/router/routesList'

export default {
    name: 'News',
    data() {
        return {
            routesList,
        }
    },
}
</script>

<style scoped></style>
