<template>
  <div>
      <li> <a :href="pokemon.url"> {{pokemon.name}} </a></li>
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

<style></style>
