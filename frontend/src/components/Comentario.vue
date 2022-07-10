<template>
    <div>
        <strong>{{ this.data['comentario'] }}</strong>
        <strong>{{ this.data['dateCreated'] }}</strong>
        <strong>{{ this.data['likes'] }}</strong>
        <div>
            <i class="fa-solid fa-thumbs-up" @click="validateLike(this.id,this.data['likes'])"></i>
            <p>{{ this.data['likes'] }}</p>
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
</style>