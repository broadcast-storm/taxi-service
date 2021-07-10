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
                        v-model="titleFilter"
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
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                        :class="{
                            'bg-yellow-500': typeFilter === '',
                            'text-gray-900': typeFilter === '',
                            'bg-gray-900': typeFilter !== '',
                            'text-yellow-500': typeFilter !== '',
                        }"
                        @click="changeFilter('')"
                    >
                        Все
                    </li>
                    <li
                        class="
                            py-2
                            px-6
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                        :class="{
                            'bg-yellow-500': typeFilter === 'news',
                            'text-gray-900': typeFilter === 'news',
                            'bg-gray-900': typeFilter !== 'news',
                            'text-yellow-500': typeFilter !== 'news',
                        }"
                        @click="changeFilter('news')"
                    >
                        Новости
                    </li>
                    <li
                        class="
                            py-2
                            px-6
                            rounded-b-md
                            md:rounded-b-none
                            rounded-t-md
                        "
                        :class="{
                            'bg-yellow-500': typeFilter === 'offer',
                            'text-gray-900': typeFilter === 'offer',
                            'bg-gray-900': typeFilter !== 'offer',
                            'text-yellow-500': typeFilter !== 'offer',
                        }"
                        @click="changeFilter('offer')"
                    >
                        Акции
                    </li>
                </ul>
            </div>
            <div
                v-if="allNewsStatus === 'loading'"
                class="h-40 flex justify-center items-center"
            >
                <Spinner />
            </div>
            <div v-if="allNewsStatus === 'success'" class="flex flex-wrap">
                <div
                    v-for="item in allNews.filter(
                        (news) =>
                            (typeFilter === '' || news.type === typeFilter) &&
                            news.title
                                .toLowerCase()
                                .includes(titleFilter.toLowerCase())
                    )"
                    :key="item.id"
                    class="news-item flex-col"
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
                            :src="item.image"
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
                            {{ item.title }}
                        </h3>
                        <h4 class="text-gray-200 text-sm text-yellow-500">
                            {{ item.type === 'offer' ? 'Акция' : 'Новость' }}
                        </h4>
                        <h4 class="mb-2 text-gray-100 text-xs">
                            {{ getClearDate(item.published_at) }}
                        </h4>
                        <p class="text-white text-sm">
                            {{ item.description }}
                        </p>
                        <div class="mt-4">
                            <router-link
                                :to="`${routesList.mainPage.children.newsPage.path}/${item.id}`"
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
                <div
                    v-if="openedNewsStatus === 'loading'"
                    class="h-40 flex justify-center items-center"
                >
                    <Spinner />
                </div>
                <div
                    v-if="openedNewsStatus === 'success'"
                    class="bg-white shadow-2xl rounded-lg mb-6 tracking-wide"
                >
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
                            :src="openedNews.image"
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
                            {{ openedNews.title }}
                        </h2>
                        <h4 class="text-gray-200 text-sm text-yellow-500">
                            {{
                                openedNews.type === 'offer'
                                    ? 'Акция'
                                    : 'Новость'
                            }}
                        </h4>
                        <h4 class="mb-2 text-gray-400 text-xs">
                            {{ getClearDate(openedNews.published_at) }}
                        </h4>
                        <p class="text-sm text-gray-700 mr-1">
                            {{ openedNews.content }}
                        </p>
                    </div>
                </div>
            </div>
        </template>
    </div>
</template>

<script>
import routesList from '@/router/routesList'
import Spinner from '@/components/Spinner'
import axios from 'axios'
export default {
    name: 'News',
    components: { Spinner },
    props: {
        id: {
            type: String,
            default: null,
        },
    },
    data() {
        return {
            routesList,
            allNewsStatus: 'loading',
            openedNewsStatus: 'loading',
            allNews: null,
            openedNews: null,
            typeFilter: '',
            titleFilter: '',
        }
    },
    computed: {},
    watch: {
        id: async function (val) {
            if (val === null) await this.getAllNews()
            else await this.getOpenedNews()
        },
    },
    async mounted() {
        if (this.id === null) await this.getAllNews()
        else await this.getOpenedNews()
    },
    methods: {
        async getAllNews() {
            try {
                const response = await axios.get(`/api/news`, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                this.allNewsStatus = 'success'
                this.allNews = response.data
            } catch (e) {
                this.allNewsStatus = 'error'
            }
        },
        async getOpenedNews() {
            try {
                const response = await axios.get(`/api/news/${this.id}`, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                this.openedNewsStatus = 'success'
                this.openedNews = response.data
            } catch (e) {
                this.openedNewsStatus = 'error'
            }
        },
        changeFilter(str) {
            this.typeFilter = str
        },
        getClearDate(str) {
            let date = new Date(str)
            const withZero = (val) => (val >= 10 ? val : '0' + val)

            return (
                withZero(date.getDate()) +
                '/' +
                withZero(date.getMonth() + 1) +
                '/' +
                date.getFullYear() +
                ' ' +
                withZero(date.getHours()) +
                ':' +
                withZero(date.getMinutes())
            )
        },
    },
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
