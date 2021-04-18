<template>
  <div class="content">
    <div>
      <ul class="pokemons">
        <li v-for="(pokemon, index) in pokemons" :key="index">
          <mc-pokemon-card :pokemon="pokemon" class="pokemon-item" />
        </li>
      </ul>
    </div>
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

  mounted() {
    this.loadPokemons();
  },

  methods: {
    loadPokemons() {
      axios
        .get(`https://pokeapi.co/api/v2/pokemon?limit=50`)
        .then((response) => response.data)
        .then((data) => data.results)
        .then((allpokemons) =>
          allpokemons.forEach((item) => this.loadPokemon(item))
        );
    },

    loadPokemon(item) {
      const url = item.url;
      axios
        .get(url)
        .then((response) => response.data)
        .then((data) => {
          const pokemon = data;
          pokemon.image = `https://pokeres.bastionbot.org/images/pokemon/${pokemon.id}.png`;
          this.pokemons.push(pokemon);
          console.log(pokemon);
        });
    },

    test() {
      console.log("testing");
      axios.get(`test`).then((response) => console.log(response));
    },
  },
};
</script>

<style scoped>
.content {

}
.pokemons {
  list-style: none;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.pokemon-item {
  margin: 0.7em;
  padding: 0.4em;
  align-self: auto;
  background-color: whitesmoke;
  border: 2px solid tomato;
  font-size: 0.8em;
  font-weight: 650;
  width: 40vh;

  display: grid;
  grid-template-columns: 50% 50%;
}
</style>
