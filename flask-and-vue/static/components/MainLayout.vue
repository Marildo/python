<template>
  <div>
    <mc-header />
    <div class="container">
         <mc-pokemons/>
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
    .container {
         min-height: 67vh;
    }
 </style>