<template>
    <div >
        <div v-if="loading ==false">
            <Movie :data="movie.data" :id="movie.id" :informationButton="false"/>
        </div>
        <div v-else class="container-spinner">
            <LoadingSpinner />
        </div>
        <hr/>
        <div v-if="loadingComentario ==false">
            <div  v-for="comentario in comentarios" :key="comentario.id">
                <Comentario :data="comentario.data" :id="comentario.id" />
            </div>
        </div>
        <div v-else class="container-spinner">
            <LoadingSpinner />
        </div>
        
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import {moviesStore,comentariosStore} from '../store/store.js';
import LoadingSpinner from './LoadingSpinner.vue';
import Comentario from './Comentario.vue';
import Movie from "./Movie.vue"
const props = defineProps ({
    id: {
        type: String,
        required: true
    }
})
const {error,movie,loading} = storeToRefs(moviesStore());
const {comentarios,loadingComentario} = storeToRefs(comentariosStore());
const { getMovieById } = moviesStore();
const { getComentarios } = comentariosStore();
getMovieById(props.id);
getComentarios(props.id);

</script>

<style scoped>
div{
    color: red;
}
.container-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
}
</style>