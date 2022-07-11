<template>
    <div class="comentarios-usuarios">
        <div class="comentario-usuario">
            <div class="comentario">
                <div class="usuario-comentario">
                    <div class="texto">
                        {{ this.data['comentario'] }}
                    </div>
                    <div class="fecha">{{ this.data['dateCreated'] }}
                    </div>
                    <div class="botonlike">
                        <button><i class="fa-solid fa-thumbs-up" @click="validateLike(this.id,this.data['likes'])"></i></button>
                        {{ this.data['likes'] }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
import { storeToRefs } from 'pinia';
import {userStore} from '../store/store.js';
const {islogged,user,loadingUser} = storeToRefs(userStore());
const classIconLike = ref('icon-deactivate');

const props = defineProps({
    id: {
        type: String,
        required: true
    },
    data: {
        type: Object,
        required: true
    }
})
const addLikesMovies = async (id, idUser) => {
    const response = await fetch(`http://localhost:5000/likes/${id}/${idUser}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const message = response.json();
    return message;
}

const removeLikeMovies = async (id, idUser) => {
    const response = await fetch(`http://localhost:5000/likes/${id}/${idUser}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const message = response;
    return message;
}

const validateLike = async (id, like) => {
    var rMessage = await addLikesMovies(id, user.value.id);
    if (rMessage.message == "like ya existe") {
        var reMessage = await removeLikeMovies(id, user.value.id);
        classIconLike.value = 'icon-activate';
        props.data['likes'] --;
        //document.getElementById(id).querySelector('.comentariolike').innerHTML--;
    } else {
        props.data['likes'] ++;
        //document.getElementById(id).querySelector('.comentariolike').innerHTML++;
    }
}
</script>

<style lang="scss" scoped>
.icon-deactivate {
    color: rgb(180, 99, 99);
}

.icon-activate {
    color: rgb(202, 52, 52);
}
.comentarios-usuarios {
    width: calc(100% - 2.5rem);
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
.comentarios-usuarios .comentario-usuario {
    display: flex;
    flex-wrap: wrap;
}
.comentarios-usuarios .usuario-comentario .texto {
    padding: 10px 15px;
    width: auto;
    display: inline-block;
    max-width: 100%;
    margin-bottom: .25rem;
    font-size: 0.9rem;
    position: relative;
    padding-right: 1.65rem;
}
.comentarios-usuarios .usuario-comentario {
    width: 100%;
    display: block;
    margin-bottom: 0.75rem;
    position: relative;
    text-align: left;
    border: 0;
    background-color: #f0f0f0;
    display: block;
    border-radius: 12px;
    margin-bottom: 0.5rem;
    padding: 5px 10px;
    font-size: medium;
}

.comentario-usuario  .fecha{
    text-align: right;
    float: right;
    font-size: small;
}
.botonlike button {
    flex-wrap: wrap;
    flex-direction: column;
    display: inline-block;
    border: 0;
    padding: 3px 8px;
    font-size: .8rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color ease-in 200ms;
}
</style>