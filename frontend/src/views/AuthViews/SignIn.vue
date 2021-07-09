<template>
    <div
        class="
            min-h-screen
            flex
            items-center
            justify-center
            bg-black bg-opacity-60
            py-6
            px-6
            sm:px-4 sm:py-12
            lg:px-8
        "
    >
        <div class="max-w-md w-full">
            <div>
                <router-link :to="routesList.mainPage.path">
                    <Logo class="h-6 sm:h-12"
                /></router-link>
                <h2
                    class="
                        mt-2
                        sm:mt-6
                        text-center text-2xl
                        font-bold
                        text-yellow-500
                    "
                >
                    Войти в аккаунт
                </h2>
            </div>
            <Alert
                v-if="error.length > 0 || tokenStatus === 'error'"
                text="Неверная почта или пароль"
            />
            <form class="mt-3 sm:mt-8" @submit.prevent="submit">
                <div class="rounded-md shadow-sm">
                    <Input
                        v-model="formData.email"
                        name="email"
                        type="email"
                        autocomplete="email"
                        required
                        placeholder="Email"
                        class="mb-2 sm:mb-3"
                    />
                    <Input
                        v-model="formData.password"
                        name="password"
                        type="password"
                        autocomplete="new-password"
                        required
                        placeholder="Пароль"
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
                        <Spinner v-if="tokenStatus === 'loading'" />
                        <span v-else>Войти</span>
                    </button>
                </div>
                <div class="flex items-center justify-center">
                    <div class="text-sm text-white">
                        Нет аккаунта?
                        <router-link
                            :to="routesList.authPage.children.signUpPage.path"
                            class="font-medium text-yellow-400 hover:text-white"
                        >
                            Зарегистрируйтесь!
                        </router-link>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import routesList from '@/router/routesList'
import Logo from '@/components/Logo'
import Input from '@/components/Input'
import Alert from '@/components/Alert'
import { AUTH_REQUEST } from '@/store/action-types/tokens'
import { mapActions, mapGetters } from 'vuex'
import Spinner from '@/components/Spinner'

export default {
    name: 'SignIn',
    components: { Logo, Input, Alert, Spinner },
    data() {
        return {
            routesList,
            formData: {
                email: '',
                password: '',
            },
            error: [],
        }
    },
    computed: {
        ...mapGetters('tokens', ['tokenStatus']),
    },
    watch: {
        formData: {
            handler() {
                if (this.error.length > 0) this.error = []
            },
            deep: true,
        },
        tokenStatus: function (val) {
            if (val === 'success') this.$router.push(routesList.mainPage.path)
        },
    },
    methods: {
        ...mapActions('tokens', [AUTH_REQUEST]),
        checkCredentials() {
            console.log(this.error)
            if (this.formData.password.length < 6)
                this.error.push('Пароль должен быть не менее 6 символов')
        },
        async submit() {
            this.checkCredentials()
            if (this.error.length === 0) {
                await this.AUTH_REQUEST({
                    email: this.formData.email,
                    password: this.formData.password,
                })
            }
        },
    },
}
</script>

<style lang="scss" scoped></style>
