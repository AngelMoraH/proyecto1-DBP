<template>
    <div class="container-movie">
        <img :src="`${this.data['imagenURL']}`" :alt="`${this.data['nombre']}`">
        <div class="container-movie__info">
            <strong class="title-movie">{{this.data['nombre']}}</strong>
            <p class="description-movie">{{this.data['description']}}</p>
            <router-link :to="`/movie/${this.id}`">más</router-link>
        </div>
    </div>
</template>

<script setup>
const props = defineProps ({
    data: {
        type: Object,
        required: true
    },
    id: {
        type: Number,
        required: true
    }
})
</script>

<style lang="scss" scoped>
.container-movie {
    border: 1px solid #000;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
    height: 20rem;
    width: 97%;
    margin: 5px 10px;
}
img {
        width: 260px;
        height: 20rem;
    }
.container-movie__info {
    padding: 10px 0px;

    width: calc(99% - 260px);
    height: calc(20rem - 20px);
}
.title-movie {
    font-size: 2rem;
    font-weight: bold;
    font-style: none;
    color: rgb(111, 0, 0);
}
a {
    text-decoration: none;
    color: rgb(111, 0, 0);
}
</style>