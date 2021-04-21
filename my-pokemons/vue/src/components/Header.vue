<template>
  <nav>
    <div class="box">
      <h1 class="title">Meus Pokemons</h1>
      <ul>
        <li><a href="#"> Favoritos </a></li>
        <li><a href="#"> Todos Pokemons</a></li>
      </ul>
    </div>
    <div>
      <img alt="Pokemons" src="../assets/banner.png" />
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
nav {
  display: grid;
  grid-template-columns: 20% 80%;
  border-bottom: 1px #355070 solid;
}
.box {
  display: grid;
  grid-template-rows: 2fr;
}

.title {
  margin: auto;
  font-size: 30px;
  font-weight: 800;
  color: dimgray;
}

ul {
  margin-bottom: 2em;
  padding: 0;
  list-style: none;
  height: 40px;
  display: grid;
  grid-template-columns: 50% 50%;
}

ul :hover {
  background-color: royalblue;
  cursor: pointer;
}

li {
  padding: 0.7em 0.2em 0.3em 0;
  margin-left: 0.1em;
  background-color: chocolate;
  text-align: center;
}

li a {
  text-decoration: none;
  color: whitesmoke;
}
</style>
