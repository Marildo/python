<template>
  <nav class="secondary-box">
    <div class="box-menu">
      <div class="title">Meus Pokemons</div>
      <ul class="menu">
        <li class="menu-item"><a href="http://"> Todos Pokemons</a></li>
        <li class="menu-item"><a href="http://">Favoritos</a></li>
      </ul>
    </div>
    <div>
      <img src="static/images/banner.png" alt="Pokemons" />
    </div>
  </nav>
</template>

<style scoped>
nav {
  height: 11rem;
  padding: 0.5em;
  display: flex;
  justify-content: start;
}

.box-menu {
  padding: 1em;
}

.title {
  text-align: center;
  font-size: 40px;
}

.menu {
  padding: 2.7em 0 0 0;
  display: flex;
  justify-content: space-between;
  list-style: none;
}

.menu-item {
  background-color: #e56b6f;
  width: 155px;
  padding: 0.3em;
  margin: 0.3em;
  font-weight: 700;
  text-align: center;
  cursor: pointer;
}

.menu-item:hover {
  background-color: tomato;
  text-decoration: underline;
}

.menu-item a {
  text-decoration: none;
  color: white;
}

img {
  height: 100%;
  width: 100%;
  border: double 4px transparent;
  border-radius: 20px;
  background-image: linear-gradient(white, white),
    radial-gradient(circle at top left, #a0c9e4, #e56b6f);
  background-origin: border-box;
  background-clip: content-box, border-box;
}
</style>
