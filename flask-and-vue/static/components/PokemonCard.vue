<template>
  <div class="pokemon-card">
    <div>
      <img :src="pokemon.image" :alt="pokemon.name" />
    </div>
    <div class="sumary">
      <div>Nome: {{ pokemon.name }}</div>
      <div>Altura: {{ pokemon.height }}</div>
      <div>Peso: {{ pokemon.weight }}</div>
      <div>Experiência: {{ pokemon.base_experience }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    pokemon: {
      required: true,
    },
  },
};
</script>

<style scoped>
img {
  width: 100%;
  height: 100%;
}

.sumary{
  padding-left: 1.2em;
  display: grid;
  grid-template-rows: 25% 25% 25% 25%;
   text-transform: capitalize;
}
</style>
