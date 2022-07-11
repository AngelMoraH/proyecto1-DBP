<script setup>
import Navbar from './components/Navbar.vue'

</script>

<template>

  <div>
    <Navbar />
    <div class="main">
      <router-view />
    </div>
  </div>
</template>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    background-image: url('./assets/fondo.jpg');
    background-size: cover;
  }
.main {
  margin-top: 90px;
}
</style>
