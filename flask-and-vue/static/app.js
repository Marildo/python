const app = Vue.createApp({
  components: {
    'mc-pokemons': Vue.defineAsyncComponent(() => loadModule('static/components/PokemonsList.vue', options))
  }
})

app.mount('#app')