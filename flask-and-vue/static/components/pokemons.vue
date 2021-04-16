<template>
  <div>
    <h4>Pokemons</h4>
    <button v-on:click="loadPokemons">Load pokemons</button>
    <ul>
      <li v-for="(pokemon, index) in pokemons" :key="index">
        {{index + 1}}: <mc-pokemon :pokemon="pokemon"></mc-pokemon>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "pokemons",

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
        .then((data) => {
          console.log(data[0]);
          this.pokemons = data;
        });
    },
  },
};
</script>

<style></style>
