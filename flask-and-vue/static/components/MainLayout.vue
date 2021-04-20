<template>
  <div>
    <mc-header />
    <div class="body-box body-content">
      <mc-pokemons />  
      <router-view></router-view>
    </div>
    <mc-footer />
  </div>
</template>

<script>
import mcHeader from "./Header.vue";
import mcPokemons from "./PokemonsList.vue";
import mcFooter from "./Fotter.vue";

export default {
  components: {
    mcHeader,
    mcPokemons,
    mcFooter,
  },
};
</script>
<style scoped>
.body-content {
  background-color: #75848e;
  min-height: 70vh;
  padding: 0.3em;
}
</style>
