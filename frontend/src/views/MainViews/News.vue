<template>
    <div>
        <h1
            class="
                text-yellow-500 text-4xl
                md:text-5xl
                xl:text-6xl
                font-bold
                mb-8
                md:mb-16
            "
        >
            Новости и Акции
        </h1>
        <template v-if="id === null">
            <div
                class="
                    border-b-2 border-gray-900
                    w-full
                    xl:w-3/4
                    flex flex-col-reverse
                    items-center
                    md:flex-row
                    justify-between
                    space-x-4
                    mb-4
                "
            >
                <div class="flex-1 w-full md:w-auto mt-4 md:mt-0">
                    <input
                        type="text"
                        class="
                            w-full
                            border-none
                            bg-transparent
                            px-2
                            text-gray-900
                            focus:outline-none focus:ring-none focus:border-none
                        "
                        placeholder="Поиск по названию"
                    />
                </div>
                <ul class="flex cursor-pointer space-x-1">
                    <li
                        class="
                            py-2
                            px-6
                            bg-yellow-500
                            text-gray-900
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                    >
                        Все
                    </li>
                    <li
                        class="
                            py-2
                            px-6
                            bg-gray-900
                            text-yellow-500
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                    >
                        Новости
                    </li>
                    <li
                        class="
                            py-2
                            px-6
                            bg-gray-900
                            text-yellow-500
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                    >
                        Акции
                    </li>
                </ul>
            </div>
            <div class="flex flex-wrap">
                <div
                    class="news-item flex-col"
                    v-for="item in news"
                    :key="item"
                >
                    <div
                        class="
                            w-full
                            h-48
                            flex
                            relative
                            overflow-hidden
                            justify-center
                            items-center
                            mr-4
                            bg-gray-300
                            rounded-t-md
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

                    <div
                        class="
                            text-left
                            p-4
                            bg-gray-900
                            rounded-b-md
                            h-44
                            flex flex-col
                            justify-between
                        "
                    >
                        <h3 class="text-white text-2xl font-bold">
                            Очень интересная акция
                        </h3>
                        <h4 class="text-gray-200 text-sm text-yellow-500">
                            Акция
                        </h4>
                        <p class="text-white text-sm">
                            Lorem ipsum dolor sit amet, consectetuer adipiscing
                            elit. Aenean commodo ligula eget dolor. Aenean
                            massa.
                        </p>
                        <div class="mt-4">
                            <router-link
                                :to="`${routesList.mainPage.children.newsPage.path}/1`"
                                class="
                                    no-underline
                                    text-yellow-500
                                    hover:text-yellow-600
                                    font-bold
                                "
                                >Подробнее...</router-link
                            >
                        </div>
                    </div>
                </div>
            </div>
        </template>
        <template v-else>
            <div class="mx-auto max-w-2xl my-20">
                <div class="bg-white shadow-2xl rounded-lg mb-6 tracking-wide">
                    <div
                        class="
                            w-full
                            h-48
                            flex
                            md:flex-shrink-0
                            relative
                            overflow-hidden
                            justify-center
                            items-center
                            mr-4
                            bg-gray-300
                            rounded-t-md
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
                    <div class="px-4 py-2 mt-2">
                        <h2
                            class="
                                font-bold
                                text-2xl text-gray-800
                                tracking-normal
                            "
                        >
                            My Amaizing Journey to the Mountains.
                        </h2>
                        <p class="text-sm text-gray-700 px-2 mr-1">
                            Lorem ipsum dolor sit amet consectetur adipisicing
                            elit. Tempora reiciendis ad architecto at aut
                            placeat quia, minus dolor praesentium officia maxime
                            deserunt porro amet ab debitis deleniti modi soluta
                            similique...
                        </p>
                        <div
                            class="flex items-center justify-between mt-2 mx-6"
                        >
                            <a href="#" class="text-blue-500 text-xs -ml-3"
                                >Show More</a
                            >
                            <a href="#" class="flex text-gray-700">
                                <svg
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    class="w-6 h-6 text-blue-500"
                                    stroke="currentColor"
                                >
                                    <path
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        stroke-width="2"
                                        d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"
                                    />
                                </svg>
                                5
                            </a>
                        </div>
                        <div class="author flex items-center -ml-3 my-3">
                            <div class="user-logo">
                                <img
                                    class="
                                        w-12
                                        h-12
                                        object-cover
                                        rounded-full
                                        mx-4
                                        shadow
                                    "
                                    src="https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=731&q=80"
                                    alt="avatar"
                                />
                            </div>
                            <h2 class="text-sm tracking-tighter text-gray-900">
                                <a href="#">By Mohammed Ibrahim</a>
                                <span class="text-gray-600">21 SEP 2015.</span>
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
import routesList from '@/router/routesList'
export default {
    name: 'News',
    components: {},
    props: {
        id: {
            type: String,
            default: null,
        },
    },
    data() {
        return {
            routesList,
            news: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        }
    },
    computed: {},

    async mounted() {
        console.log(this.id)
    },

    methods: {},
}
</script>

<style lang="scss" scoped>
.news-item {
    width: calc(100% - 0.5rem);
    margin: 0.25rem;
}
@media (min-width: 1024px) {
    .news-item {
        width: calc(100% / 2 - 0.5rem);
        margin: 0.25rem;
    }
}
@media (min-width: 1536px) {
    .news-item {
        width: calc(100% / 3 - 0.5rem);
        margin: 0.25rem;
    }
}
</style>
