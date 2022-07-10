<template>
    <div>


        <div class = "form">
                <h2 class = "form_tittle">Register</h2>
                <p class = "form_paragraph">¿Ya tienes una cuenta?

                    <a class = "form_link" href="/">Entra aqui</a>
                    <!-- <button class = "form_submit" @click="funcionLogin()">Ingresar</button> -->

                </p>
                <div class = "form_container">

                    <div class = "form_group">
                        <input class ="form_input" type="text" placeholder="" v-model="username">
                        <label for="usuario" class = form_label>Nombre de usuario</label>
                        <span class = "form_line"></span>
                    </div>
                

                    <div class = "form_group">
                        <input class ="form_input" type="text" placeholder="" v-model="email">
                        <label for="contrasena" class = form_label>Email</label>
                        <span class = "form_line"></span>
                     </div>


                     <div class = "form_group">
                        <input class ="form_input" :type="tipe" placeholder="" v-model="password">
                        <label for="usuario" class = form_label>Contrasena</label>
                        <div class = "icon">
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
                        </div>
                        <span class = "form_line"></span>
                    </div>
                    
                    <button class ='form_submit' @click="funcionRegister()">Registrarse</button>


                </div>



            </div>

        
    </div>
</template>

<script setup>
import { ref } from "@vue/runtime-core";
import { storeToRefs } from 'pinia';
import router from "../router/routes.js";
import {userStore} from '../store/store.js';

let username=ref("");
let email = ref("");
let password = ref("");
let tipe = ref("password");
const {islogged,user,loadingUser,errorUser,messageUser} = storeToRefs(userStore());
const {register} = userStore();

const showPassword = () => {
    if (tipe.value == "password") {
        tipe.value = "text";
    } else {
        tipe.value = "password";
    }
};

const funcionRegister = async() => {
    if (username.value == "" || email.value == "" || password.value == "") {
        alert("username, email o password vacios");
    } else{
        await register(username.value,email.value,password.value);
        if(messageUser.value == "usuario o email ya existe"){
            alert(messageUser.value);
        }else{
            router.push('/login');
        }

    }
};
</script>


<style lang="scss" scoped>
.form_submit{
    background: #9b2222;
    color: #fff;
    font-family: 'Roboto', sans-serif;
    font-weight: 300;
    font-size: 1rem;
    padding: .8em 0;
    border: none;
    border-radius: .5em;
    width: 100%;
    padding: .6em .3em;
}
.icon{
    position: absolute;
    height: 60%;
    position: absolute;
    top: 50%;
    right: 8px;
    transform: translateY(-50%);
    opacity: 0.3;
    cursor: pointer;
}
.container{
    background-color: #fff;
    margin: auto;
    width: 90%;
    max-width: 400px;
    padding: 4.5em 3 em;
    border-radius: 10px;
    box-shadow: 0 5px 10px -5px rgb(0 0 0/ 30%);
    text-align: center;
}
.body{
    font-family: 'Roboto', sans-serif;
    background-color: #e5e5f7;
    background-size: 20px 20px;
    background-position: 0 0, 10px 10px;
    display: flex;
    min-height: 100vh;
}

.form{
    background-color: rgba(252, 252, 252, 0.747);
    margin: auto;
    width: 90%;
    max-width: 400px;
    padding: 4.5em 3em;
    border-radius: 10px;
    box-shadow: 0 5px 10px -5px rgb(0 0 0/ 30%) ;
    text-align: center;
}
.form_container{
    margin-top: 2em;
    display: grid;
    gap: 2.5em;

}

.form_tittle{
    font-size: 2rem;
    margin-bottom: .5em
}.form_paragraph{
    font-weight: 300;
    
}.form_link{
    font-weight: 400;
    color: #000;
}.form_group{
    position: relative;
    --color: #5757577e;

}.form_input{
    width: 100%;
    background: none;
    color: #706c6c;
    font-size: 1rem;
    padding: .6em .3em;
    border: none;
    outline: none;
    border-bottom: 1px solid var(--color);
    font-family: 'Roboto', sans-serif;
}
.form_line{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: #3866f2;
    transform: scale(0);
    transform: left bottom;
    transition: transform .4s;
}
.form_label{
    color: var(--valor);
    cursor: pointer;
    position: absolute;
    top: 0;
    left: 5px;
    transform: translateY(10);
    transition: transform .5s, color .3s;

}

.form_input:not(:placeholder-shown){
    color: #706c6c;
}

.form_input:focus +.form_label, 
.form_input:not(:placeholder-shown)+.form_label{
    transform: translateY(-12px) scale(.7);
    transform-origin: left top;
    color: #8b1b1b;
} 

.form_line{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: #3866f2;
    transform: scale(0);
    transform: left bottom;
    transition: transform .4s;

}

.form_group{
    position: relative;
    --color: #5757577e;
}

// .form_input:focus~.form_line,
// .form_input:not(:placeholder-shown)~.form_line{
//     transform: scale(1);
// }


.form_label{
    color: var(--color);
    cursor: pointer;
    position:absolute;
    top: 0;
    left: 5px;
    transform: translateY(10px);
    transition: transform .5s, color .3s;
}


.form_line{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 1px;
    background-color: #9e0808;
    transform: scale(0);
    transform: left bottom;
    transition: transform .4s;
}

// .form_input:focus ~ .form_line,
// .form_input:not(:placeholder-shown) ~ .form_line{
//     transform: scale(1);
// }

</style>