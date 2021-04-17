<template>
  <div>
    <h4>Todos Pokemons</h4>
    <button v-on:click="loadPokemons" type="button" class="btn btn-primary">
      Load pokemons
    </button>
    <button v-on:click="test" type="button" class="btn btn-warning">
      Test
    </button>

    <ul v-for="(pokemon, index) in pokemons" :key="index">
      <mc-pokemon-card :pokemon="pokemon" /> 
    </ul>
  </div>
</template>

<script>
import mcPokemonCard from "./PokemonCard.vue";

export default { 
  name: "pokemons",
  components: { mcPokemonCard },

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
        .then((data) => (this.pokemons = data));
    },

    test() {
      console.log("testing");
      axios.get(`test`).then((response) => console.log(response));
    },
  },
};
</script>

<style></style>
