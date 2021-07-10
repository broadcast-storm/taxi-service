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
            Водители
        </h1>
        <div class="w-full lg:w-9/12 mx-auto mb-4">
            <span class="text-lg font-bold text-gray-900"
                >Здесь представлен список водителей, которые работают сегодня
                <br />
                <span v-if="driversStatus === 'success'"
                    >(Сейчас {{ drivers.length }})</span
                >
            </span>
        </div>
        <div
            v-if="driversStatus === 'loading'"
            class="h-40 flex justify-center items-center"
        >
            <Spinner />
        </div>
        <div
            v-if="driversStatus === 'success'"
            class="flex flex-wrap w-full lg:w-9/12 mx-auto"
        >
            <div
                v-for="(item, index) in drivers"
                :key="index"
                class="
                    w-full
                    md:w-1/2
                    xl:w-1/3
                    border-4 border-transparent
                    flex-col
                    p-4
                "
            >
                <div
                    class="
                        w-full
                        h-32
                        flex
                        relative
                        overflow-hidden
                        justify-center
                        items-center
                        bg-gray-900
                        rounded-t-md
                        text-yellow-500
                        p-4
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
                    <h3 class="text-white text-2xl text-center font-bold">
                        {{
                            item.user_details.name +
                            ' ' +
                            item.user_details.surname
                        }}
                    </h3>
                    <h4 class="text-gray-200 text-sm">
                        Автомобиль:
                        {{
                            car_colors[item.car_details.color] +
                            ' ' +
                            car_brands[item.car_details.brand]
                        }}
                    </h4>
                    <h4 class="text-gray-200 text-sm">
                        Статус:
                        <span class="text-yellow-500">{{
                            item.driverStatus === 'waiting_order'
                                ? 'Ожидает клиента'
                                : 'Отвозит клиента'
                        }}</span>
                    </h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import routesList from '@/router/routesList'
import Spinner from '@/components/Spinner'
import axios from 'axios'

export default {
    name: 'Drivers',
    components: { Spinner },
    data() {
        return {
            routesList,
            driversStatus: 'loading',
            drivers: null,
            car_colors: {
                yellow: 'желтый',
                green: 'зеленый',
                red: 'красный',
                black: 'черный',
                white: 'белый',
                blue: 'синий',
            },
            car_brands: {
                BMW: 'BMW',
                LADA: 'Lada',
                CHEVROLET: 'Chevrolet',
                HYUNDAI: 'Hyundai',
                MERCEDES: 'Mercedes',
                PEUGEOT: 'Peugeot',
            },
        }
    },
    computed: {},

    async mounted() {
        await this.getDrivers()
    },

    methods: {
        async getDrivers() {
            try {
                const response = await axios.get(`/api/drivers`, {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                this.driversStatus = 'success'
                this.drivers = response.data
            } catch (e) {
                this.driversStatus = 'error'
            }
        },
    },
}
</script>

<style lang="scss" scoped></style>
