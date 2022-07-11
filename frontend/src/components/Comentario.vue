<template>
    <div class="comentarios-usuarios">
        <div class="comentario-usuario"> 
            <div class="usuario">{{user['userName']}}</div>
            
            <div class="texto">
                {{ this.data['comentario'] }}
            </div>
            <div class="botonlike">
                <button><i class="fa-solid fa-thumbs-up" @click="validateLike(this.id,this.data['likes'])"></i>{{ this.data['likes'] }}</button>
                
            </div>
            <div class="fecha">{{ this.data['dateCreated'] }}
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

.comentarios-usuarios {
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    width: 100%;
}
.comentarios-usuarios .comentario-usuario {
    display: block;
    flex-wrap: wrap;
    background-color: #fff;
    margin-top: 10px;
    margin: 10px;
    border-radius: 12px;
}
.comentarios-usuarios .comentario-usuario .usuario {
    text-align: left;
    margin-left: 20px;
    margin-top: 5px;
}
.comentarios-usuarios .comentario-usuario .fecha{
    text-align: right;
    float: right;
    font-size: small;
    margin-right: 5px;
}
.comentarios-usuarios .comentario-usuario .texto{
    margin-left: 10px;
    margin-right: 10px;
    border: 0;
    background-color: #f0f0f0;
    display: flex;
    border-radius: 12px;
    margin-bottom: 5px;
    padding: 10px 20px;
    margin-top: 5px;
    text-align: left;
}

.comentarios-usuarios .botonlike button{
    display: flex;
    border: 0;
    padding: 8px 15px;
    border-radius: 8px;
    transition: background-color .5s;
    cursor: pointer;
}
.comentarios-usuarios .botonlike i {
    margin-right: .5rem;
    
}
.comentarios-usuarios .botonlike {
    display: flex;
    border: 0;
    padding: 0px 15px;
    border-radius: 8px;
    
}
.comentarios-usuarios .botonlike button:hover{
    background-color: rgba(46, 47, 53, 0.369);
}

/*.comentarios-usuarios .comentario-usuario .usuario-comentario .texto {
    padding: 10px 15px;
    width: auto;
    display: inline-block;
    max-width: 100%;
    margin-bottom: .25rem;
    font-size: 0.9rem;
    position: relative;
    padding-right: 1.65rem;
}*/

/*.comentarios-usuarios .usuario-comentario {
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

.comentarios-usuarios .comentario-usuario  .fecha{
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
}*/
</style>