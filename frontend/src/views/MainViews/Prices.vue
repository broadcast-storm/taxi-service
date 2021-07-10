<template>
    <div class="">
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
            Цены
        </h1>
        <div class="w-full lg:w-9/12 mx-auto mb-4">
            <span class="text-lg font-bold text-gray-900"
                >Тариф с 15.04.2021</span
            >
        </div>

        <table class="table-fixed w-full lg:w-9/12 mx-auto custom-table">
            <thead>
                <tr>
                    <th
                        class="
                            w-1/2
                            p-2
                            md:p-4
                            text-left text-white text-base
                            lg:text-lg
                            bg-gray-900
                        "
                    >
                        Услуга
                    </th>
                    <th
                        class="
                            w-1/2
                            md:w-1/4
                            p-2
                            md:p-4
                            text-center text-white text-base
                            lg:text-lg
                            bg-gray-900
                        "
                    >
                        Стоимость
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in tariffPrices" :key="index" class="">
                    <td class="w-1/2 p-2 md:p-4">{{ item.name }}</td>
                    <td class="w-1/4 p-2 md:p-4 text-center">
                        {{ item.price }}
                        {{
                            item.type === 'rub'
                                ? 'руб.'
                                : item.type === 'min'
                                ? 'мин.'
                                : '%'
                        }}
                    </td>
                </tr>
            </tbody>
        </table>
        <div class="w-full lg:w-9/12 mx-auto my-4">
            <span class="text-lg md:text-xl font-bold text-yellow-500"
                >В тарифе приведена таблица примерной стоимости проезда
                (рассчитана до населенных пунктов от центра г.Раменское)</span
            >
        </div>
        <table class="table-fixed w-full lg:w-9/12 mx-auto custom-table">
            <thead>
                <tr>
                    <th
                        class="
                            w-1/2
                            p-2
                            md:p-4
                            text-left text-white text-base
                            lg:text-lg
                            bg-gray-900
                        "
                    >
                        Пункт назначения
                    </th>
                    <th
                        class="
                            w-1/2
                            md:w-1/4
                            p-2
                            md:p-4
                            text-center text-white text-base
                            lg:text-lg
                            bg-gray-900
                        "
                    >
                        Стоимость
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in placePrices" :key="index" class="">
                    <td class="w-1/2 p-2 md:p-4">{{ item.name }}</td>
                    <td class="w-1/4 p-2 md:p-4 text-center">
                        {{ item.price }}
                        руб
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import routesList from '@/router/routesList'

export default {
    name: 'MainPage',
    components: {},
    data() {
        return {
            routesList,
            tariffPrices: [
                {
                    name: 'Остановка по пути следования (влючено 3 мин.)',
                    price: 30,
                    type: 'rub',
                },
                {
                    name: 'По г.Раменское (включен вызов и проезд 1 км.)',
                    price: 90,
                    type: 'rub',
                },
                {
                    name: 'Ожидание пассажира более установленного времени при подаче автомобиля за 1 мин.',
                    price: 10,
                    type: 'rub',
                },
                {
                    name: 'Багаж более 50 кг. или не вмещающийся в багажник автомобиля',
                    price: 90,
                    type: 'rub',
                },
                {
                    name: 'Бесплатное ожидание пассажира (при подаче / для предварительного заказа) автомобиля',
                    price: 10,
                    type: 'min',
                },
                {
                    name: 'Обратная дорога с пассажиром - от тарифа при условии, что обратная дорога в г.Раменское, и стоимость проезда в одном направлении более 400р.',
                    price: 50,
                    type: 'per',
                },
            ],
            placePrices: [
                {
                    name: 'Минино',
                    price: 500,
                },
                {
                    name: 'Гжель',
                    price: 650,
                },
                {
                    name: 'Коняшино',
                    price: 700,
                },
                {
                    name: 'Григорово',
                    price: 550,
                },
            ],
        }
    },
    computed: {},

    async mounted() {},

    methods: {},
}
</script>

<style lang="scss" scoped>
.custom-table {
    border-collapse: collapse;
    th,
    td {
        border: 2px solid #111827;
    }
}
</style>
