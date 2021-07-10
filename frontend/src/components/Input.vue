<template>
    <div>
        <label :for="name" class="sr-only">{{ name }}</label>
        <input
            :id="name"
            :name="name"
            :type="type"
            :pattern="pattern === '' ? null : pattern"
            :autocomplete="autocomplete"
            :required="required"
            class="
                relative
                block
                w-full
                px-3
                py-2
                sm:py-3
                bg-black bg-opacity-30
                border-2 border-gray-300
                placeholder-gray-500
                text-base text-gray-300
                rounded-md
                h-14
                focus:outline-none focus:ring-yellow-500 focus:border-yellow-500
            "
            :class="{
                'text-white': darkMode,
                'bg-gray-900': darkMode,
                'border-gray-200': darkMode,
                'bg-opacity-100': darkMode,
            }"
            :placeholder="placeholder"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>

<script>
export default {
    name: 'Input',
    components: {},
    props: {
        modelValue: { type: String, default: '' },
        required: {
            type: Boolean,
            default: false,
        },
        name: {
            type: String,
            required: true,
        },
        darkMode: {
            type: Boolean,
            default: false,
        },
        placeholder: {
            type: String,
            default: 'Placeholder',
        },
        autocomplete: {
            type: String,
            default: 'off',
        },
        pattern: {
            type: String,
            default: '',
        },
        type: {
            validator(value) {
                return [
                    'checkbox',
                    'hidden',
                    'password',
                    'radio',
                    'text',
                    'email',
                    'number',
                    'tel',
                    'datetime-local',
                ].includes(value)
            },
            default: 'text',
        },
    },
    computed: {},
    methods: {},
}
</script>

<style></style>
