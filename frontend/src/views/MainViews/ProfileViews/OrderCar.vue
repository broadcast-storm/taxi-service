<template>
    <form @submit.prevent="submit" v-if="orderInfo === null">
        <div
            class="
                flex flex-col
                sm:flex-row sm:justify-between
                md:justify-start md:flex-col
            "
        >
            <div>
                <h2 class="text-yellow-500 text-4xl font-bold mb-4">Откуда</h2>
                <div class="flex justify-start flex-col md:flex-row">
                    <div>
                        <span class="pl-2 block">Населенный пункт</span>
                        <div class="relative inline-flex self-center">
                            <svg
                                class="
                                    text-white
                                    bg-yellow-500
                                    absolute
                                    top-0
                                    right-0
                                    m-2
                                    pointer-events-none
                                    p-2
                                    h-8
                                    w-8
                                    rounded
                                "
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 38 22"
                                version="1.1"
                            >
                                <g
                                    id="ZahnhelferDE—Design"
                                    stroke="none"
                                    stroke-width="1"
                                    fill="none"
                                    fill-rule="evenodd"
                                >
                                    <g
                                        id="ZahnhelferDE–Icon&amp;Asset-Download"
                                        transform="translate(-539.000000, -199.000000)"
                                        fill="#ffffff"
                                        fill-rule="nonzero"
                                    >
                                        <g
                                            id="Icon-/-ArrowRight-Copy-2"
                                            transform="translate(538.000000, 183.521208)"
                                        >
                                            <polygon
                                                id="Path-Copy"
                                                transform="translate(20.000000, 18.384776) rotate(135.000000) translate(-20.000000, -18.384776) "
                                                points="33 5.38477631 33 31.3847763 29 31.3847763 28.999 9.38379168 7 9.38477631 7 5.38477631"
                                            />
                                        </g>
                                    </g>
                                </g>
                            </svg>
                            <select
                                v-model="formData.town"
                                class="
                                    custom-select
                                    text-lg
                                    rounded-md
                                    border-2
                                    text-white
                                    w-60
                                    h-14
                                    px-3
                                    py-2
                                    sm:py-3
                                    bg-gray-900
                                    hover:border-yellow-500
                                    focus:outline-none
                                    appearance-none
                                "
                                required
                            >
                                <option
                                    v-for="(item, index) in towns"
                                    :key="index"
                                    :value="index"
                                >
                                    {{ item }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <div class="w-52 md:w-auto">
                        <span class="pl-2">Улица</span>
                        <Input
                            v-model="formData.street"
                            name="street"
                            type="text"
                            required
                            placeholder="Улица"
                            dark-mode
                        />
                    </div>
                    <div class="w-20">
                        <span class="pl-2">Дом</span>
                        <Input
                            v-model="formData.house"
                            name="house"
                            type="number"
                            required
                            placeholder="Дом"
                            dark-mode
                        />
                    </div>
                    <div class="w-20">
                        <span class="pl-2">Подъезд</span>
                        <Input
                            v-model="formData.entrance"
                            name="entrance"
                            type="number"
                            required
                            placeholder="Подъезд"
                            dark-mode
                        />
                    </div>
                </div>
            </div>
            <div>
                <h2 class="text-yellow-500 text-4xl font-bold mb-4">Куда</h2>
                <div class="flex justify-start flex-col md:flex-row">
                    <div>
                        <span class="pl-2 block">Населенный пункт</span>
                        <div class="relative inline-flex self-center">
                            <svg
                                class="
                                    text-white
                                    bg-yellow-500
                                    absolute
                                    top-0
                                    right-0
                                    m-2
                                    pointer-events-none
                                    p-2
                                    h-8
                                    w-8
                                    rounded
                                "
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 38 22"
                                version="1.1"
                            >
                                <g
                                    id="ZahnhelferDE—Design"
                                    stroke="none"
                                    stroke-width="1"
                                    fill="none"
                                    fill-rule="evenodd"
                                >
                                    <g
                                        id="ZahnhelferDE–Icon&amp;Asset-Download"
                                        transform="translate(-539.000000, -199.000000)"
                                        fill="#ffffff"
                                        fill-rule="nonzero"
                                    >
                                        <g
                                            id="Icon-/-ArrowRight-Copy-2"
                                            transform="translate(538.000000, 183.521208)"
                                        >
                                            <polygon
                                                id="Path-Copy"
                                                transform="translate(20.000000, 18.384776) rotate(135.000000) translate(-20.000000, -18.384776) "
                                                points="33 5.38477631 33 31.3847763 29 31.3847763 28.999 9.38379168 7 9.38477631 7 5.38477631"
                                            />
                                        </g>
                                    </g>
                                </g>
                            </svg>
                            <select
                                v-model="formData.destinationTown"
                                class="
                                    custom-select
                                    text-lg
                                    rounded-md
                                    border-2
                                    text-white
                                    w-60
                                    h-14
                                    px-3
                                    py-2
                                    sm:py-3
                                    bg-gray-900
                                    hover:border-yellow-500
                                    focus:outline-none
                                    appearance-none
                                "
                                required
                            >
                                <option
                                    v-for="(item, index) in towns"
                                    :key="index"
                                    :value="index"
                                >
                                    {{ item }}
                                </option>
                            </select>
                        </div>
                    </div>
                    <div class="w-52 md:w-auto">
                        <span class="pl-2">Улица</span>
                        <Input
                            v-model="formData.destinationStreet"
                            name="street"
                            type="text"
                            required
                            placeholder="Улица"
                            dark-mode
                        />
                    </div>
                    <div class="w-20">
                        <span class="pl-2">Дом</span>
                        <Input
                            v-model="formData.destinationHouse"
                            name="house"
                            type="number"
                            required
                            placeholder="Дом"
                            dark-mode
                        />
                    </div>
                </div>
            </div>
        </div>
        <div class="mt-4">
            <div class="w-1/2 md:w-1/4">
                <span class="pl-2">Промо код</span>
                <Input
                    v-model="formData.discount"
                    name="promo"
                    type="text"
                    placeholder="Промо код"
                    dark-mode
                />
            </div>
            <div class="w-1/2 md:w-1/4">
                <span class="pl-2">Время</span>
                <Input
                    v-model="formData.scheduledTime"
                    name="time"
                    type="datetime-local"
                    dark-mode
                    required
                />
            </div>
        </div>
        <div>
            <button
                type="submit"
                class="
                    group
                    relative
                    w-full
                    sm:w-1/2
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
            >
                <span class="flex items-center">
                    <Spinner v-if="sendOrderStatus === 'loading'" />
                    <span v-else>Заказать такси</span>
                </span>
            </button>
        </div>
    </form>
    <div
        v-if="orderInfo !== null"
        class="rounded-md bg-gray-900 text-white p-4"
    >
        <div class="text-2xl mb-4">Информация о текущем заказе</div>
        <div class="text-yellow-500 text-2xl font-bold mb-4">Откуда</div>
        <div class="mb-4">{{ orderInfo.full_client_address }}</div>
        <div class="text-yellow-500 text-2xl font-bold mb-4">Куда</div>
        <div class="mb-4">{{ orderInfo.full_destination_address }}</div>
        <div class="mb-4">
            Время прибытия такси:
            <span class="text-yellow-500">{{
                getClearDate(orderInfo.scheduledTime)
            }}</span>
        </div>
        <div>
            Автомобиль:
            {{
                car_colors[orderInfo.driver_details.car_details.color] +
                ' ' +
                car_brands[orderInfo.driver_details.car_details.brand]
            }}
        </div>
        <div>
            Водитель:
            {{ orderInfo.driver_details.user_details.name }}
        </div>
        <div class="mb-4">
            Статус:
            <span class="text-yellow-500">{{
                order_status[orderInfo.orderStatus]
            }}</span>
        </div>
        <div class="mb-2">
            Цена поездки:
            <span
                class="text-lg pl-4"
                :class="{
                    'line-through': orderInfo.discount_details !== null,
                    'font-bold': orderInfo.discount_details === null,
                }"
                >{{ orderInfo.price }} руб</span
            >
            <span v-if="orderInfo.discount_details !== null" class="pl-2"
                ><br />
                Со скидкой в
                {{ orderInfo.discount_details.discountAmount }}%:</span
            >
            <span
                v-if="orderInfo.discount_details !== null"
                class="pl-2 text-lg font-bold text-yellow-500"
                >{{
                    orderInfo.price -
                    orderInfo.price *
                        (orderInfo.discount_details.discountAmount / 100)
                }}
                руб</span
            >
        </div>
    </div>
    <div v-if="orderInfo !== null">
        <button
            class="
                group
                relative
                w-full
                sm:w-1/2
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
            @click="closeCurrentOrder"
        >
            <span class="flex items-center">
                <Spinner v-if="closeOrderStatus === 'loading'" />
                <span v-else>Отменить заказ</span>
            </span>
        </button>
    </div>
</template>

<script>
import Input from '@/components/Input'
import Spinner from '@/components/Spinner'
import routesList from '@/router/routesList'
import { mapGetters } from 'vuex'
import axios from 'axios'
import jwt from 'jsonwebtoken'
export default {
    name: 'OrderCar',
    components: { Input, Spinner },
    data() {
        return {
            routesList,
            orderInfo: null,
            formData: {
                discount: '',
                town: 'Ramenskoe',
                street: '',
                house: '',
                entrance: '1',
                destinationTown: 'Ramenskoe',
                destinationStreet: '',
                destinationHouse: '',
                scheduledTime: '',
            },
            towns: {
                Ramenskoe: 'Раменское',
                Kratovo: 'Кратово',
                Zukovski: 'Жуковский',
                Bronici: 'Броницы',
                Minino: 'Минино',
                Ghel: 'Гжель',
                Kosherovo: 'Кошерово',
                Konyashino: 'Коняшино',
            },
            order_status: {
                client_waiting: 'Водитель едет',
                driver_waiting: 'Водитель ждет',
                client_canceled: 'Вы отменили заказ',
                in_progress: 'Водитель отвозит вас',
                completed: 'Вы на месте!',
            },
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
            showSuccessAlert: false,
            sendOrderStatus: '',
            closeOrderStatus: '',
            checkCurrentOrderStatus: 'loading',
            error: [],
        }
    },
    computed: {
        ...mapGetters('tokens', ['getAccessToken']),
    },

    watch: {
        formData: {
            handler() {
                if (this.error.length > 0) this.error = []
            },
            deep: true,
        },
        sendOrderStatus: function (val) {
            if (val === 'success') {
                this.showSuccessAlert = true
                setTimeout(() => (this.showSuccessAlert = false), 1500)
            }
        },
    },
    async mounted() {
        await this.checkCurrentOrder()
    },
    methods: {
        checkCredentials() {
            console.log('')
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
        async submit() {
            this.checkCredentials()
            if (this.error.length === 0) {
                try {
                    this.sendOrderStatus = 'loading'
                    const token = this.getAccessToken
                    const userId = jwt.decode(token).user_id
                    await axios.post(
                        `/api/create-order`,
                        {
                            order: {
                                user_id: userId,
                                discount: this.formData.discount,
                                town: this.formData.town,
                                street: this.formData.street,
                                house: this.formData.house,
                                entrance: this.formData.entrance,
                                destinationTown: this.formData.destinationTown,
                                destinationStreet:
                                    this.formData.destinationStreet,
                                destinationHouse:
                                    this.formData.destinationHouse,
                                scheduledTime: this.formData.scheduledTime,
                            },
                        },
                        {
                            headers: {
                                'Content-Type': 'application/json',
                                Authorization: `Bearer ${token}`,
                            },
                        }
                    )

                    await this.checkCurrentOrder()
                } catch (e) {
                    this.lastNewsStatus = 'error'
                }
            }
        },
        async checkCurrentOrder() {
            try {
                this.checkCurrentOrderStatus = 'loading'
                const token = this.getAccessToken
                const response = await axios.get(`/api/current-order`, {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${token}`,
                    },
                })

                this.checkCurrentOrderStatus = 'success'
                if (response.data.orderStatus !== null)
                    this.orderInfo = response.data
            } catch (e) {
                this.lastNewsStatus = 'error'
            }
        },
        async closeCurrentOrder() {
            try {
                this.closeOrderStatus = 'loading'
                const token = this.getAccessToken
                await axios.post(
                    `/api/close-order`,
                    {
                        id: this.orderInfo.id,
                    },
                    {
                        headers: {
                            'Content-Type': 'application/json',
                            Authorization: `Bearer ${token}`,
                        },
                    }
                )
                this.clearForm()
                this.closeOrderStatus = 'success'
                this.orderInfo = null
            } catch (e) {
                this.lastNewsStatus = 'error'
            }
        },
        clearForm() {
            this.formData = {
                discount: '',
                town: 'Ramenskoe',
                street: '',
                house: '',
                entrance: '1',
                destinationTown: 'Ramenskoe',
                destinationStreet: '',
                destinationHouse: '',
                scheduledTime: '',
            }
        },
    },
}
</script>

<style scoped></style>
