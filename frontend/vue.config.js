module.exports = {
    css: {
        loaderOptions: {
            scss: {
                additionalData: `@import "~@/styles/styles.scss";`,
            },
        },
    },
    chainWebpack: (config) => {
        const svgRule = config.module.rule('svg')

        svgRule.uses.clear()

        svgRule
            .use('babel-loader')
            .loader('babel-loader')
            .end()
            .use('vue-svg-loader')
            .loader('vue-svg-loader')
            .options({
                svgo: {
                    plugins: [
                        { removeDimensions: true },
                        { removeViewBox: false },
                    ],
                },
            })
    },
    devServer: {
        proxy: {
            '^/api/': {
                target: 'http://127.0.0.1:8000/',
                ws: false,
            },
        },
    },
    // outputDir must be added to Django's TEMPLATE_DIRS
    outputDir: './dist/',
    // assetsDir must match Django's STATIC_URL
    assetsDir: 'static',
}
