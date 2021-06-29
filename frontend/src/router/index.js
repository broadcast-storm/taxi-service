import { createRouter, createWebHistory } from 'vue-router'
import routesList from '@/router/routesList'
import store from '../store'

const routes = [
    {
        path: routesList.mainPage.path,
        component: () => import('@/views/Main.vue'),
        children: [
            {
                path: routesList.mainPage.path,
                component: () => import('@/views/MainViews/MainPage.vue'),
            },
            {
                path: routesList.mainPage.children.profilePage.path,
                component: () => import('@/views/MainViews/Profile.vue'),
                meta: {
                    requiresAuthentication: true,
                },
            },
            {
                path: routesList.mainPage.children.pricesPage.path,
                component: () => import('@/views/MainViews/Prices.vue'),
            },
            {
                path: routesList.mainPage.children.driversPage.path,
                component: () => import('@/views/MainViews/Drivers.vue'),
            },
            {
                path: routesList.mainPage.children.newsPage.path,
                component: () => import('@/views/MainViews/News.vue'),
            },
        ],
    },
    {
        path: routesList.authPage.path,
        component: () => import('@/views/Auth.vue'),
        children: [
            {
                path: routesList.authPage.children.signInPage.path,
                component: () => import('@/views/AuthViews/SignIn.vue'),

                meta: {
                    requiresToBeLoggedOut: true,
                },
            },
            {
                path: routesList.authPage.children.forgotPasswordPage.path,
                component: () => import('@/views/AuthViews/ForgotPassword.vue'),

                meta: {
                    requiresToBeLoggedOut: true,
                },
            },
            {
                path: routesList.authPage.children.signUpPage.path,
                component: () => import('@/views/AuthViews/SignUp.vue'),

                meta: {
                    requiresToBeLoggedOut: true,
                },
            },
        ],
    },
]

const history = createWebHistory(process.env.BASE_URL)
const router = createRouter({ routes, history })

router.beforeEach((to, from, next) => {
    if (to.meta.requiresToBeLoggedOut) {
        if (store.getters['tokens/isAuthenticated']) {
            next(routesList.mainPage.path)
        } else {
            next()
        }
    } else if (to.meta.requiresAuthentication) {
        if (!store.getters['tokens/isAuthenticated']) {
            next(routesList.authPage.children.signInPage.path)
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router
