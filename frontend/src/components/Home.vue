<template>
    <div class="container-body">
        <div class="container-input__search">
            <input type="text" class="input-search" placeholder="Buscar..." v-model="pelicula" @keyup.enter="searchMovie(pelicula)">
            
            <p v-if="pelicula.length>0">Press Enter</p>
        </div>
        <div v-if="loading" class="container-spinner">
            <LoadingSpinner />
        </div>
        <div v-else >
            <div v-for="movie in movies" :key="movie.id">
                <Movie :data="movie['data']" :id="movie.id" :informationButton="true" />
            </div>
            <div>
                <input type="button" value="1" @click="getMovies(1)" />
                <input type="button" value="2" @click="getMovies(2)" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from "@vue/runtime-core";
import {moviesStore} from '../store/store.js';
import Movie from "./Movie.vue";
import LoadingSpinner from "./LoadingSpinner.vue"
import { storeToRefs } from 'pinia';
let pelicula = ref("");

const {error,movies,loading} = storeToRefs(moviesStore());
const {getMovies,searchMovie} = moviesStore();

onMounted(() => {
    getMovies(1);
});


</script>

<style scoped>
.container-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
}


.container-input__search {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

i {
    font-size: 2rem;
    color: rgb(111, 0, 0);
}
.input-search {
    width: 60%;
    outline: none;
    height: 50px;
    border: 2px solid rgba(170, 20, 20, 0.315);
    border-radius: 35px;
    padding: 10px;
    font-size: 1.5rem;
    font-weight: bold;
    font-style: none;
    color: rgb(111, 0, 0);
}

.input-search:focus {
    border: 2px solid rgb(170, 20, 20);
}

.input-search::placeholder {
    color: rgba(135, 9, 9, 0.919);
}
p {
    margin-left: 10px;
    font-size: 1.5rem;
    font-weight: bold;
    font-style: none;
    color: rgb(79, 0, 0);
}
</style>