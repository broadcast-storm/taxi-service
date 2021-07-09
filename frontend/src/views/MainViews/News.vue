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
                <router-link
                    class="
                        flex
                        items-center
                        mb-4
                        text-gray-900
                        hover:text-yellow-500
                    "
                    :to="routesList.mainPage.children.newsPage.path"
                >
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        x="0px"
                        y="0px"
                        viewBox="0 0 512 512"
                        class="h-4 fill-current mr-2"
                    >
                        <g>
                            <g>
                                <path
                                    d="M492,236H68.442l70.164-69.824c7.829-7.792,7.859-20.455,0.067-28.284c-7.792-7.83-20.456-7.859-28.285-0.068
			l-104.504,104c-0.007,0.006-0.012,0.013-0.018,0.019c-7.809,7.792-7.834,20.496-0.002,28.314c0.007,0.006,0.012,0.013,0.018,0.019
			l104.504,104c7.828,7.79,20.492,7.763,28.285-0.068c7.792-7.829,7.762-20.492-0.067-28.284L68.442,276H492
			c11.046,0,20-8.954,20-20C512,244.954,503.046,236,492,236z"
                                />
                            </g>
                        </g></svg
                    ><span>Назад к новостям</span>
                </router-link>
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
                    <div class="px-4 py-4 mt-2">
                        <h2
                            class="
                                font-bold
                                text-2xl text-gray-800
                                tracking-normal
                            "
                        >
                            My Amaizing Journey to the Mountains.
                        </h2>
                        <span class="py-8 text-gray-500"> 22/08/2000 </span>
                        <p class="text-sm text-gray-700 mr-1">
                            Lorem ipsum dolor sit amet consectetur adipisicing
                            elit. Tempora reiciendis ad architecto at aut
                            placeat quia, minus dolor praesentium officia maxime
                            deserunt porro amet ab debitis deleniti modi soluta
                            similique...
                        </p>
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
