<template>
    <div>
        <div v-if="loading == false" class="details">
            <Movie :data="movie.data" :id="movie.id" :informationButton="false" />
        </div>
        <div v-else class="container-spinner">
            <LoadingSpinner />
        </div>
        <hr />
        <div class="container-input">
            <div class="user-box">
                <input type="text" name="" required v-model="comentario">
                <label>Ingrese su Comentario</label>
                <button @click="addComentarios()">submit</button>
            </div>
        </div>
        <div v-if="loadingComentario == false" class="comentario-usuario">
            <div v-for="comentario in comentarios" :key="comentario.id">
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
import { moviesStore, comentariosStore,userStore } from '../store/store.js';
import LoadingSpinner from '../components/LoadingSpinner.vue';
import Comentario from '../components/Comentario.vue';
import Movie from "../components/Movie.vue";
import { ref } from '@vue/runtime-core';
let comentario = ref('');
const props = defineProps({
    id: {
        type: String,
        required: true
    }
})
const { error, movie, loading } = storeToRefs(moviesStore());
const { islogged, user, loadingUser } = storeToRefs(userStore());
const { comentarios, loadingComentario,errorComentario } = storeToRefs(comentariosStore());
const { getMovieById } = moviesStore();
const { getComentarios,addComentario } = comentariosStore();
getMovieById(props.id);
getComentarios(props.id);
async function addComentarios(){
    if(comentario.value == ''){
        alert('Ingrese un comentario');
    }else{
        await addComentario(comentario.value,user.value.id,parseInt(props.id));
        comentario.value = '';
    }
}
</script>

<style scoped>
.details {
    color: red;
}

.container-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 50px;
}
button {
    background-color: #8f0606;
    color: white;
    padding: 10px 20px;
    margin: 8px 0;
    border: 2px solid #8f0606;
    border-radius: 7px;
    cursor: pointer;
    font-size: 26px;
    width: 20%;
    transition: border-radius 0.3s ease-in-out,border 0.3s ease-in-out, color 0.3s ease-in-out,background-color 0.6s ease-in-out;
}
button:hover{
    background-color: transparent;
    color: #8f0606;
    padding: 10px 20px;
    margin: 8px 0;
    border: 2px solid #8f0606;
    border-radius: 9px;
    cursor: pointer;
    font-size: 26px;
    width: 20%;
}
.comentario-usuario {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    margin-bottom: 1.5rem;
    padding: 18px;
    background-color: #fff;
    box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
    border-radius: 12px;
}

.user-box {
    position: relative;
    margin:10px;
}

.user-box input {
    width: 90%;
    height: 36px;
    padding: 10px 10px 3px 10px;
    font-size: 16px;
    color: #2c3e50;
    border: none;
    border-radius: 35px;
    outline: none;
    background: rgb(197, 197, 197);
}

.user-box label {
    position: absolute;
    top: 5px;
    left: 70px;
    padding: 10px 0;
    font-size: 16px;
    color: #c20000;
    pointer-events: none;
    transition: .5s;
}

.user-box input:focus~label,
.user-box input:valid~label {
    top: -4.6px;
    left: 70px;
    color: #8d0808;
    font-size: 10px;
    font-weight: bolder;
}

</style>