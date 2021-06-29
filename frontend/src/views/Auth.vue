<template>
    <div class="auth-background">
        <router-view />
    </div>
</template>

<script>
export default {
    name: 'Auth',
}
</script>

<style lang="scss" scoped>
.auth-background {
    height: 100vh;
    background-image: url('~@/assets/img/auth/background.jpg');
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
}
</style>
