<template>
    <div class="login-box">
        <div class="container-poster">
            <img :src="imgURL" alt="poster" class="poster">
            <div class="button2" @click="addMovie()">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                Submit
            </div>
        </div>
        <div class="container-info">
            <h2>NUEVA PELICULA</h2>
            <div class="user-box">
                <input type="text" name="" required v-model="titulo">
                <label>Titulo</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="descripcion">
                <label>Descripcion</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="estreno">
                <label>Estreno</label>
            </div>
            <div class="user-box">
                <input type="url" name="" required v-model="imgURL">
                <label>Poster</label>
            </div>
            <div class="user-box">
                <span id="rangeValue" v-text="`calificacion: ${calificacion}`"></span>
                <input class="range" type="range" min="0.0" max="10.0" step="0.1" v-model="calificacion" />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
import { storeToRefs } from 'pinia';
import { userStore } from '../store/store.js';
import { useRoute, useRouter } from 'vue-router';

const router = useRouter();
const route = useRoute();
const { user } = storeToRefs(userStore());
let titulo = ref("");
let descripcion = ref("");
let calificacion = ref(0.0);
let estreno = ref("");
let imgURL = ref("https://www.nato-pa.int/sites/default/files/default_images/default-image.jpg");

const addMovie = async () => {
    if (titulo.value == "" || descripcion.value == "" || estreno.value == "" || imgURL.value == "" ) {
        alert("Todos los campos son obligatorios");
    } else {
        const response = await fetch(`http://localhost:5000/movies/${user.value.rol}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                'data': {
                    nombre: titulo.value,
                    description: descripcion.value,
                    calificacion: calificacion.value,
                    fechaEstreno: estreno.value,
                    imagenURL: imgURL.value
                }
            })
        });
        const data = await response.json();
        console.log(data.success);
        if (data['success']) {
            alert("Pelicula agregada con exito");
        } else {
            alert("Error al agregar pelicula");
        }
    }
};
</script>

<style lang="scss" scoped>
.login-box {
    position: absolute;
    display: flex;
    top: 57%;
    left: 50%;
    width: 80%;
    height: 500px;
    padding: 20px 5px 2px;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    transform: translate(-50%, -50%);
    background: rgb(105, 0, 0);
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0, 0, 0, .6);
    border-radius: 10px;
}

#rangeValue {
    position: relative;
    display: block;
    text-align: center;
    color: #999;
}

.container-info {
    width: 40%;
}

.container-poster {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 50%;
    height: 100%;
}

.poster {
    width: 300px;
    height: 350px;
}

.login-box h2 {
    margin: 0 0 30px;
    padding: 0;
    color: #fff;
    text-align: center;
}

.login-box .user-box {
    position: relative;
}

.login-box .user-box input {
    width: 100%;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    margin-bottom: 30px;
    border: none;
    border-bottom: 1px solid #fff;
    outline: none;
    background: transparent;
}

.login-box .user-box label {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10px 0;
    font-size: 16px;
    color: #fff;
    pointer-events: none;
    transition: .5s;
}

.login-box .user-box input:focus~label,
.login-box .user-box input:valid~label {
    top: -20px;
    left: 0;
    color: #b9b9b9;
    font-size: 12px;
}


.button2 {
    position: relative;
    display: inline-block;
    padding: 20px 61px;
    border-radius: 4px;
    color: #ffffff;
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
                background: linear-gradient(90deg, transparent, #ffa47d);
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
                background: linear-gradient(180deg, transparent, #88b0ff);
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

                background: linear-gradient(270deg, transparent, #c8ff7b);
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
                background: linear-gradient(360deg, transparent, #ff98f6);
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