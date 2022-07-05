<template>
    <div >
        hola {{this.id}}
        {{movie}}
    </div>
</template>

<script setup>
import { storeToRefs } from 'pinia';
import {moviesStore} from '../store/store.js';
const props = defineProps ({
    id: {
        type: String,
        required: true
    }
})
const {error,movie,loading} = storeToRefs(moviesStore());
const { getMovieById } = moviesStore();
getMovieById(props.id);


</script>

<style scoped>
div{
    color: red;
}
</style>