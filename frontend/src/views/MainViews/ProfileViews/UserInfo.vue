<template>
    <Alert
        v-if="error.length > 0 || profileUpdateStatus === 'error'"
        :text="
            profileUpdateStatus === 'error'
                ? 'Введеный номер уже используется\n'
                : '' + error.join('\n')
        "
    />
    <Alert
        v-if="showSuccessAlert"
        :text="'Данные успешно изменены'"
        class="bg-green-100 border border-green-400 text-green-700"
    />
    <form class="mt-3 sm:mt-8" @submit.prevent="submit">
        <div class="rounded-md shadow-sm">
            <Input
                v-model="formData.name"
                name="firstName"
                type="text"
                autocomplete="name"
                required
                placeholder="Имя"
                dark-mode
                class="mb-2 sm:mb-3"
            />
            <Input
                v-model="formData.surname"
                name="surname"
                type="text"
                autocomplete="surname"
                required
                placeholder="Фамилия"
                dark-mode
                class="mb-2 sm:mb-3"
            />
            <Input
                v-model="formData.phone"
                name="phone"
                type="tel"
                autocomplete="phone"
                pattern="(\+7[-_()\s]+|\+7\s?[(]{0,1}[0-9]{3}[)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2})"
                required
                placeholder="+7(___)___-__-__"
                dark-mode
                class="mb-2 sm:mb-3"
            />
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
                    <Spinner v-if="profileUpdateStatus === 'loading'" />
                    <span v-else>Сохранить изменения</span>
                </span>
            </button>
        </div>
    </form>
</template>

<script>
import Input from '@/components/Input'
import routesList from '@/router/routesList'
import Spinner from '@/components/Spinner'
import { mapActions, mapGetters } from 'vuex'
import { PROFILE_UPDATE } from '@/store/action-types/profile'
import Alert from '@/components/Alert'
export default {
    name: 'UserInfo',
    components: { Input, Spinner, Alert },
    data() {
        return {
            routesList,
            formData: {
                name: '',
                surname: '',
                phone: '+7(___)___-__-__',
            },
            showSuccessAlert: false,
            updatingStatus: '',
            error: [],
        }
    },
    computed: {
        ...mapGetters('profile', ['profileUpdateStatus', 'profileInfo']),
    },

    watch: {
        formData: {
            handler() {
                if (this.error.length > 0) this.error = []
            },
            deep: true,
        },
        profileUpdateStatus: function (val) {
            if (val === 'success') {
                this.showSuccessAlert = true
                setTimeout(() => (this.showSuccessAlert = false), 1500)
            }
        },
    },
    async mounted() {
        this.formData.name = this.profileInfo.name
        this.formData.surname = this.profileInfo.surname
        this.formData.phone = this.profileInfo.phone || ''
    },
    methods: {
        ...mapActions('profile', [PROFILE_UPDATE]),
        checkCredentials() {
            console.log(this.error)
            if (
                this.formData.name.length === 0 ||
                this.formData.surname.length === 0 ||
                this.formData.phone.length === 0
            )
                this.error.push('Нельзя отправить пустые поля')
            if (
                !/^\+7\s?[(]?9[0-9]{2}[)]?\s?\d{3}[-]?\d{2}[-]?\d{2}$/.test(
                    this.formData.phone
                )
            ) {
                this.error.push('Неверно введен номер')
            }
        },
        async submit() {
            this.checkCredentials()
            if (this.error.length === 0) {
                await this.PROFILE_UPDATE({
                    name: this.formData.name,
                    surname: this.formData.surname,
                    phone: this.formData.phone,
                })
            }
        },
    },
}
</script>

<style scoped></style>
