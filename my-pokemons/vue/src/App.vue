<template>
  <div>    
    <MainLayout />
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Hello World Vue!" />
  
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import MainLayout from './components/MainLayout.vue';


export default {
  name: "App",
  components: {

    HelloWorld,
    MainLayout,
  },

  data() {
    return {
      pa: "/img/logo.png",
    };
  },

  mounted() {},

  methods: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
