<template>
  <div class="content">
    <div>
      <ul class="pokemons">
        <li v-for="(pokemon, index) in pokemons" :key="index">
          <mc-pokemon-card :pokemon="pokemon" class="pokemon-item" />
        </li>
      </ul>
    </div>
    <nav aria-label="Page navigation">
      <ul class="pagination justify-content-end pk-cursor">
        <li class="page-item">
          <a class="page-link" aria-label="Previous" @click="nav('previous')">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li
          class="page-item"
          :class="{ active: currentPage == page }"
          v-for="page in pages"
          :key="page"
        >
          <a class="page-link" @click="nav(page)">{{ page }}</a>
        </li>
        <li class="page-item">
          <a class="page-link" aria-label="Next" @click="nav('next')">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
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
      offset: 0,
      limit: 12,
      pages: [],
      currentPage: 1,
    };
  },

  mounted() {
    this.loadPokemons(`https://pokeapi.co/api/v2/pokemon/?offset=0&limit=12`);
  },

  methods: {
    loadPokemons(url) {
      console.log(url);
      axios
        .get(url)
        .then((response) => response.data)
        .then((data) => data.results)
        .then((allpokemons) => {
          this.pokemons = [];
          this.pagination();
          allpokemons.forEach((item) => this.loadPokemon(item));
        });
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
        });
    },

    nav(value) {
      if (value == "next") {
        this.currentPage++;
      } else if (value == "previous") {
        this.currentPage--;
      } else {
        this.currentPage = value;
      }

      if (this.offset < 0) {
        this.offset = 0;
      }

      this.offset = this.currentPage * this.limit;

      console.log("Current Page: ", this.currentPage);
      console.log("Offset: ", this.offset);

      const url = `https://pokeapi.co/api/v2/pokemon/?offset=${this.offset}&limit=${this.limit}`;
      console.log(url);
      this.loadPokemons(url);
    },

    pagination() {
      this.pages = [];

      let start = this.currentPage - 5;
      if (start < 1) {
        start = 1;
      }
      const stop = start + 9
      console.log('start: ',start, 'stop: ',stop  )

      for (let index = start; index < stop; index++) {
        this.pages.push(index);
      }
    },

    test() {
      console.log("testing");
      axios.get(`test`).then((response) => console.log(response));
    },
  },
};
</script>

<style scoped>
.pokemons {
  list-style: none;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  margin: 0px;
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

.pk-cursor {
  cursor: pointer;
}
</style>
