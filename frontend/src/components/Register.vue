<template>
    <div>
        <h1>Register</h1>
        <input type="text" placeholder="username" v-model="username">
        <input type="text" placeholder="email" v-model="email">
        <input :type="tipe" placeholder="password" v-model="password">
        <div v-if="tipe=='password'">
            <button @click="showPassword()">
                <i  class="fa-solid fa-eye-slash" ></i>
            </button>
        </div>
        <div v-else>
            <button @click="showPassword()">
                <i class="fa-solid fa-eye" ></i>
            </button>
        </div>
        
        {{email}} - {{password}}
        <button @click="funcionRegister()">Login</button>
        <div v-if="user !=null">
            {{user}}
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue-demi";
import { storeToRefs } from 'pinia';
import {userStore} from '../store/store.js';

let username=ref("");
let email = ref("");
let password = ref("");
let tipe = ref("password");
const {islogged,user,loadingUser} = storeToRefs(userStore());
const {register} = userStore();

const showPassword = () => {
    if (tipe.value == "password") {
        tipe.value = "text";
    } else {
        tipe.value = "password";
    }
};

const funcionRegister = () => {
    register(username.value,email.value,password.value);
    route.push("/");
};
</script>

<style lang="scss" scoped>
button{
    background-color: transparent;
    border: none;
}
</style>