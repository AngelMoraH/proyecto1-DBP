<template>
    <div >
        <div v-if="loading ==false" class="details">
            <Movie :data="movie.data" :id="movie.id" :informationButton="false"/>
        </div>
        <div v-else class="container-spinner">
            <LoadingSpinner />
        </div>
        <hr/>
        <div v-if="loadingComentario ==false" class="comentario-usuario">
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
import LoadingSpinner from '../components/LoadingSpinner.vue';
import Comentario from '../components/Comentario.vue';
import Movie from "../components/Movie.vue";
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
.details{
    color: red;
}
.container-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
}
.comentario-usuario {
    justify-content: left;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    margin-bottom: 1.5rem;
    padding: 18px;
    background-color: #fff;
    box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
    border-radius: 12px;
}
</style>