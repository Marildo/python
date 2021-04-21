<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png" />
    <h1>Auqi</h1>

    <HelloWorld msg="Hello World Vue" />
  
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";


export default {
  name: "App",
  components: {

    HelloWorld,
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
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
