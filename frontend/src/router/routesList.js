const routesList = {
    mainPage: {
        path: '/',
        header: 'Главная',
        children: {
            newsPage: {
                path: '/news',
                children: {
                    openedNews: {
                        path: '/news/:id',
                    },
                },
            },
            pricesPage: {
                path: '/prices',
            },
            driversPage: {
                path: '/drivers',
            },
            profilePage: {
                path: '/profile',
                header: 'Профиль',
                children: {
                    editUser: {
                        path: '/profile',
                    },
                    orderCar: {
                        path: '/profile/order-car',
                    },
                },
            },
        },
    },
    authPage: {
        path: '/auth',
        header: 'Авторизация',
        children: {
            signInPage: {
                path: '/auth/sign-in',
            },
            forgotPasswordPage: {
                path: '/auth/forgot-password',
            },
            signUpPage: {
                path: '/auth/sign-up',
            },
        },
    },
}

export default routesList
