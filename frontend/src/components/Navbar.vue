<template>
    <header class="header">
        <div class="container">
            <router-link to="/">
                <strong class="navfont" style="color:rgb(233, 233, 233)">HORRORPEDIA</strong>
            </router-link>
            <input type="checkbox" id="toggle" class="input-toggler">
            <label for="toggle" class="menu-toggler">
                <span class="menu-toggler-line"></span>
                <span class="menu-toggler-line"></span>
                <span class="menu-toggler-line"></span>
            </label>

            <aside class="sidebar">
                <ul class="menu" v-if="user!=null">
                    <li>
                        <router-link to="/"><span class="menu-link">Home</span>
                        </router-link>
                    </li>
                    <li v-if="user['userName'] == 'angel' && user['email'] == 'angel456mora123@gmail.com'">
                        <router-link to="/addmovie"><span class="menu-link">add movie</span>
                        </router-link>
                    </li>
                    <li>
                        <div class="button2" @click="functionLogOut()">
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            Adiós {{ user['userName'] }}
                        </div>
                    </li>
                </ul>
                <ul class="menu" v-else>
                    <li>
                        <router-link to="/"><span class="menu-link">Home</span>
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/login"><span class="menu-link">Ingresa</span>
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/register"><span class="menu-link">Registrate</span>
                        </router-link>
                    </li>
                </ul>
            </aside>
        </div>
    </header>
</template>



<script setup>
import { storeToRefs } from 'pinia';
import { useRoute, useRouter } from 'vue-router';
import { userStore } from '../store/store.js';
const { islogged, user, loadingUser } = storeToRefs(userStore());
const { logout } = userStore();
const router = useRouter();
const route = useRoute();

const functionLogOut = async () => {
    await logout();
    console.log(islogged.value);
    await window.localStorage.removeItem("user");
    router.push('/login')

};
</script>

<style lang="scss" scoped>
:root {
    --color-1: #90080c;
}

.header {
    background-color: #84090f;
    height: 80px;
    width: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1;
    padding: 5px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.25);
}

.navfont {
    font-size: 60px;
    font-weight: bold;
    font-style: none;
    font-family: 'Creepster', cursive;
}

strong,
li {
    text-decoration: none;
}

.container {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.nav ul {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    padding: 5px;
    list-style: none;
}

.nav-menu {
    display: flex;
    margin-right: 40px;
    list-style: none;
}

a {
    text-decoration: none;
    color: #fff;
}

.nav-menu-item {
    font-size: 18px;
    margin: 0 10px;
    line-height: 80px;
    text-transform: uppercase;
    width: max-content;
}

.nav-menu-link {
    padding: 8px 12px;
    border-radius: 3px;
    transition: all 0.5s;
}

.nav-menu-link:hover,
.nav-menu-link_active {
    background-color: #034574;
    transition: all 0.5s;
}


legend,
label,
input,
ul,
li {
    margin: 0;
    padding: 0;
}

ul,
li {
    list-style: none;
}

a {
    text-decoration: none;
}

.input-toggler {
    display: none;
}

.menu-toggler {
    position: absolute;
    right: 0px;
    top: 0px;
    width: 80px;
    height: 65px;
    background: transparent;
    z-index: 100;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    cursor: pointer;
}

.menu-toggler-line {
    width: 60%;
    height: 3px;
    background: #ffc;
    margin: 0 0 10px 0px;
    position: relative;
    transition: all .40s ease-out;
}

.menu-toggler:hover {
    .menu-toggler-line {
        background: #ffbb84;
    }

}

.input-toggler:checked~.menu-toggler .menu-toggler-line {
    top: 5px;
    translateY: 100px;
    transform: rotate(45deg);

}

.input-toggler:checked~.menu-toggler .menu-toggler-line:nth-child(2) {
    display: none;

}

.input-toggler:checked~.menu-toggler .menu-toggler-line:nth-child(3) {
    top: -5px;
    translateY: 10;
    transform: rotate(135deg);
}



.nav ul {
    width: 100%;
}

.nav ul li {
    width: 100%;
    text-align: center;
}

.nav ul li a {
    display: inline-block;
    font-size: 26px;
    color: #fff;
    text-transform: uppercase;
}

.sidebar {
    position: absolute;
    top: 0;
    height: 100vh;
    width: 100%;
    background: #000;
    opacity: 0.5;

    display: flex;
    justify-content: center;
    align-items: center;

    transform: translateX(-300%);

    transition: all .40s ease-out;
}

.menu-link {
    color: white;
    font-size: 10vmin;
    line-height: 15vmin;
    -webkit-transition: all .25s ease-out;
    transition: all .25s ease-out;
}

.menu-link:hover,
.menu-link:focus,
.menu-link:active {
    color: #84090f;
}

.input-toggler:checked~.sidebar {
    transform: translateX(-1%);
    opacity: .98;
    width: 100%;
}

.button2 {
    position: relative;
    display: inline-block;
    padding: 20px 61px;
    border-radius: 4px;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    overflow: hidden;
    margin: 25px;
    font-family: "Roboto", sans-serif;
    filter: hue-rotate(0deg);
    border: 2px solid #d2bdff;
    transition: all 0.1s linear;

    &:hover {
        cursor: pointer;
        border: 1px solid transparent;

        span {
            position: absolute;
            display: block;

            &:nth-child(1) {
                filter: hue-rotate(0deg);
                top: 0;
                left: 0;
                width: 100%;
                height: 3px;
                background: linear-gradient(90deg, transparent, #3a86ff);
                animation: animate1 1s linear infinite;
            }

            @keyframes animate1 {
                0% {
                    left: -100%;
                }

                50%,
                100% {
                    left: 100%;
                }
            }

            &:nth-child(2) {
                filter: hue-rotate(60deg);
                top: -100%;
                right: 0;
                width: 3px;
                height: 100%;
                background: linear-gradient(180deg, transparent, #3a86ff);
                animation: animate2 1s linear infinite;
                animation-delay: 0.25s;
            }

            @keyframes animate2 {
                0% {
                    top: -100%;
                }

                50%,
                100% {
                    top: 100%;
                }
            }

            &:nth-child(3) {
                filter: hue-rotate(120deg);
                bottom: 0;
                right: 0;
                width: 100%;

                background: linear-gradient(270deg, transparent, #3a86ff);
                animation: animate3 1s linear infinite;
                animation-delay: 0.5s;
            }

            @keyframes animate3 {
                0% {
                    right: -100%;
                    height: 3px;
                }

                50%,
                100% {
                    height: 2px;
                    right: 100%;
                }
            }

            &:nth-child(4) {
                filter: hue-rotate(300deg);
                bottom: -100%;
                left: 0;
                width: 3px;
                height: 100%;
                background: linear-gradient(360deg, transparent, #3a86ff);
                animation: animate4 1s linear infinite;
                animation-delay: 0.75s;
            }

            @keyframes animate4 {
                0% {
                    bottom: -100%;
                }

                50%,
                100% {
                    bottom: 100%;
                }
            }
        }
    }
}
</style>