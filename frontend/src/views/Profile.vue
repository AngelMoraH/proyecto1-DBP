<template>
    <div class="div-profile">
        <div class="container-profile">
            <img src="https://ps.w.org/user-avatar-reloaded/assets/icon-256x256.png?rev=2540745" alt="avatar">
            <div class="container-info">
                <span>userName: {{user['userName']}}</span>
                <span>email: {{user['email']}}</span>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
import { storeToRefs } from "pinia";
import { userStore } from "../store/store.js";
const { islogged, user, loadingUser } = storeToRefs(userStore());
</script>

<style lang="scss" scoped>

.container-profile {
    position: absolute;
    top: 20%;
    right: 15%;
    left: 15%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    height: 30rem;
    width: 60rem;
    background-color: #f0efef;
    border-radius: 35px;
}
.container-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
span {
    font-size: 1.5rem;
    font-weight: bold;
    color: #000;
}
</style>
