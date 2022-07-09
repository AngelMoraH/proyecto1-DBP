<template>
    <div class="login-box">
        <div class="container-poster">
            <img :src="imgURL" alt="poster" class="poster">
            <div class="button2" @click="addMovie()">
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                HOVER ME
            </div>
        </div>
        <div class="container-info">
            <h2>NUEVA PELICULA</h2>
            <div class="user-box">
                <input type="text" name="" required v-model="titulo">
                <label>Titulo</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="autor">
                <label>Autor</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="descripcion">
                <label>Descripcion</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="calificacion">
                <label>Calificacion</label>
            </div>
            <div class="user-box">
                <input type="text" name="" required v-model="estreno">
                <label>Estreno</label>
            </div>
            <div class="user-box">
                <input type="url" name="" required v-model="imgURL">
                <label>Poster</label>
            </div>

        </div>
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
let titulo = ref("");
let autor = ref("");
let descripcion = ref("");
let calificacion = ref("");
let estreno = ref("");
let imgURL = ref("https://www.nato-pa.int/sites/default/files/default_images/default-image.jpg");

const data = {
    titulo,
    autor,
    descripcion,
    calificacion,
    estreno,
    imgURL
};

const addMovie = async () => {
    const response = await fetch("http://localhost:3000/movies", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({'data': data})
    });
    const json = await response.json();
    console.log(json);
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
    padding: 20px 5px;
    flex-direction: row;
    justify-content: space-evenly;
    transform: translate(-50%, -50%);
    background: rgba(0, 0, 0, 1);
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0, 0, 0, .6);
    border-radius: 10px;
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
    width: 350px;
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
    color: #03e9f4;
    font-size: 12px;
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