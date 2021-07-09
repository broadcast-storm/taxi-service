<template>
    <div
        class="
            bg-red-100
            border border-red-400
            text-red-700
            px-2
            sm:px-4
            py-1
            sm:py-3
            my-1
            sm:my-3
            rounded
            relative
        "
        role="alert"
    >
        <span>{{ text }}</span>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    components: {},
    props: {
        text: { type: String, default: '' },
    },
    computed: {},
    methods: {},
}
</script>
