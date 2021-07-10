<template>
    <div class="space-y-4">
        <span class="text-4xl font-bold text-yellow-500">Пробки</span>
        <div class="overflow-hidden relative h-72 rounded bg-gray-300">
            <a
                href="https://yandex.ru/maps?utm_medium=mapframe&utm_source=maps"
                style="
                    color: #eee;
                    font-size: 12px;
                    position: absolute;
                    top: 0px;
                "
            ></a
            ><a
                href="https://yandex.ru/maps/geo/ramenskoye/53063474/?l=trf%2Ctrfe&ll=38.321408%2C55.555119&utm_medium=mapframe&utm_source=maps&z=11.52"
                style="
                    color: #eee;
                    font-size: 12px;
                    position: absolute;
                    top: 14px;
                "
            ></a
            ><iframe
                src="https://yandex.ru/map-widget/v1/-/CCUeuDxh9B"
                frameborder="1"
                allowfullscreen="true"
                class="w-full h-full relative"
            ></iframe>
        </div>
    </div>
</template>
<script>
export default {
    name: 'TrafficJam',
    components: {},
    computed: {},

    async mounted() {},

    methods: {},
}
</script>
