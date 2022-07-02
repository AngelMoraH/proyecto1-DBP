<template>
    <div class="container-body">
        <div class="container-input__search">
            <input type="text" class="input-search" placeholder="Buscar..." v-model="pelicula" @keyup.enter="searchMovie(pelicula)">
            
            <p v-if="pelicula.length>0">Press Enter</p>
        </div>
        <div v-if="loading" class="container-spinner">
            <div class="spinner"></div>
        </div>
        <div v-else v-for="movie in data.value" :key="movie.id">
            <Movie :data="movie.data" :id="movie.id" />
        </div>
        <div>
            <input type="button" value="1" @click="getMovies(1)" />
            <input type="button" value="2" @click="getMovies(2)" />
        </div>
    </div>
</template>

<script setup>
import { onMounted, reactive, ref } from "@vue/runtime-core";
import Movie from "./Movie.vue";
let data = reactive([]);
let loading = ref(true);
let pelicula = ref("");
const baseURL = "http://localhost:5000/";
function getMovies(page) {
    loading.value = true;
    fetch(baseURL + `movies?page=${page}`).then(response => response.json()).then(json => {
        data.value = json['movies'];
        console.log(data.value);
        loading.value = false;
    }).catch(error => {
        console.log(error);
    });

}

const searchMovie = (title) => {
    data.value = [];
    loading.value = true;
    fetch(baseURL + `movies?search=${title}`).then(response => response.json()).then(json => {
        data.value = json['movies'];
        console.log(data.value);
        loading.value = false;
    }).catch(error => {
        console.log(error);
    });
}

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