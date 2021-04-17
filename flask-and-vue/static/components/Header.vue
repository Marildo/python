<template>
  <nav>
    <div class="container">
      <div class="row">
        <span class="col-3"> Meus Pokemons </span>
        <div class="col-9">
          <img src="static/images/banner.png" alt="Pokemons" />
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
nav {
  background-color: #355070;
  height: 15rem;
  padding: 1em;
}

span {
  font-family: fantasy;
  text-align: center;
  font-size: 60px;
  color: #e56b6f;
  padding: auto;
}

img {
  height: 100%;
  width: 100%;
  border: double 4px transparent;
  border-radius: 20px;
  background-image: linear-gradient(white, white), radial-gradient(circle at top left,  #A0C9E4,#e56b6f);
  background-origin: border-box;
  background-clip: content-box, border-box;
}
</style>
