<template>
  <div id="app">
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">Menu</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="#logo">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#modelParams">Model Params</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#simulationParams">Simulation Params</a>
      </li>
    </ul>
    <span class="navbar-text">
      iss project sejsja zima 2021
    </span>
  </div>
  </nav>

    <img id="logo" alt="PP logo" src="./assets/Logo_PP.png">
    <HelloWorld msg="Projekt ISS"/>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #00587c;
}

</style>
