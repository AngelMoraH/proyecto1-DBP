<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
/**
 * <nav>
      <router-link to="/">Home</router-link>&nbsp;
      <router-link to="/about">Acerca de</router-link>
    </nav>
 */
import HelloWorld from './components/HelloWorld.vue'
import Navbar from './components/Navbar.vue'

</script>

<template>

  <div>
    <Navbar />
    <div style="margin-top: 100px;">
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
}
</style>
