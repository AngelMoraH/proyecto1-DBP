<template>
    <div>
        <h1>Login</h1>
        <input type="text" placeholder="email" v-model="email">
        <input :type="tipe" placeholder="password" v-model="password">
        <div v-if="tipe == 'password'">
            <button @click="showPassword()">
                <i class="fa-solid fa-eye-slash"></i>
            </button>
        </div>
        <div v-else>
            <button @click="showPassword()">
                <i class="fa-solid fa-eye"></i>
            </button>
        </div>

        <button @click="funcionLogin()">Login</button>
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
import { storeToRefs } from 'pinia';
import { useRoute, useRouter } from 'vue-router';
import { userStore } from '../store/store.js';

let email = ref("");
let password = ref("");
let tipe = ref("password");
const { islogged, user, loadingUser } = storeToRefs(userStore());
const { login } = userStore();
const router = useRouter();
const route = useRoute();

const showPassword = () => {
    if (tipe.value == "password") {
        tipe.value = "text";
    } else {
        tipe.value = "password";
    }
};

const funcionLogin = async () => {
    if (email.value == "" || password.value == "") {
        alert("email o password vacios");
    }else {
        await login(email.value, password.value);
        router.push('/');
    }

};
</script>

<style lang="scss" scoped>
button {
    background-color: transparent;
    border: none;
}
</style>