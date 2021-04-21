<template>
 <img alt="Vue logo" src="./assets/logo.png" /> 
  
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import filters from './utils/filters.js'

export default {
  name: "App",
  components: {
    HelloWorld,
  },

  data(){
    return {
      pa:'/img/logo.png'
    }
  },

  mounted(){
     
  },

  methods: {
    load2(img) {
      return filters.loadImage(img)
    },
  },
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
