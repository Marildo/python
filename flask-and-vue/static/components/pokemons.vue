<template>
  <div>
    <h4>Pokemons</h4>
    <button v-on:click="loadPokemons" type="button" class="btn btn-primary">Load pokemons</button>
    <ul  v-for="(pokemon, index) in pokemons" :key="index">
         <mc-pokemon :pokemon="pokemon"></mc-pokemon>
    </ul>
    
    

  </div>
</template>

<script>

import mcPokemon from './pokemon.vue'

export default {
  name: "pokemons",
  components: { mcPokemon },

  data() {
    return {
      pokemons: [],
    };
  },

  methods: {
    loadPokemons() {
      console.log("carregando");
      axios
        .get(`https://pokeapi.co/api/v2/pokemon?limit=100`)
        .then((response) => response.data.results)
        .then((data) =>    this.pokemons = data);
    },
  },
};
</script>

<style></style>
