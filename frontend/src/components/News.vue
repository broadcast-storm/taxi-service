<template>
    <div class="space-y-4 relative">
        <span class="text-4xl font-bold text-yellow-500">Новости</span>
        <div
            v-if="lastNewsStatus === 'loading'"
            class="h-40 flex justify-center items-center"
        >
            <Spinner />
        </div>

        <div
            v-if="lastNewsStatus === 'success'"
            class="flex flex-col lg:flex-row"
        >
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
                    :src="lastNewsInfo.image"
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
                    {{ lastNewsInfo.title }}
                </h3>
                <h4 class="mb-2 text-sm text-yellow-500">
                    {{ lastNewsInfo.type === 'offer' ? 'Акция' : 'Новость' }}
                </h4>
                <h4 class="mb-2 text-gray-100 text-xs">
                    {{ getClearDate(lastNewsInfo.published_at) }}
                </h4>
                <p class="text-white text-sm">
                    {{ lastNewsInfo.description }}
                </p>
                <div class="mt-4">
                    <router-link
                        :to="`${routesList.mainPage.children.newsPage.path}/${lastNewsInfo.id}`"
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
import Spinner from '@/components/Spinner'
import axios from 'axios'

export default {
    name: 'News',
    components: { Spinner },
    data() {
        return {
            routesList,
            lastNewsStatus: 'loading',
            lastNewsInfo: null,
        }
    },

    async mounted() {
        await this.getLatestNews()
    },

    methods: {
        async getLatestNews() {
            try {
                const response = await axios.get(`/api/last-news`, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                this.lastNewsStatus = 'success'
                this.lastNewsInfo = response.data
            } catch (e) {
                this.lastNewsStatus = 'error'
            }
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

<style scoped></style>
