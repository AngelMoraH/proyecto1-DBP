<template>
    <div>
        <div class="spinner"></div>
    </div>
</template>


<style lang="scss" scoped>
.spinner {
    border: 4px solid rgba(103, 12, 12, 0.512);
    width: 46px;
    height: 46px;
    border-radius: 50%;
    border-left-color: rgb(154, 0, 0);
    animation: spin 1s ease infinite;
}

@keyframes spin {
    0% {

        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

</style>