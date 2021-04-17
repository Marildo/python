const vueApp = {
    delimiters: ['[[', ']]'],

    data() {
        return {
            message: 'Hello Vue!!',
            pokemons: [
                'Blue', 'Gold', 'Diamond'
            ]
        }
    },

    methods: {
        addPokemon() {
            this.pokemons.push(this.message)
        }
    }
}

const options = {
    moduleCache: {
      vue: Vue
    },

    async getFile(url) {
      const res = await fetch(url);
      console.log(url, res)  
      if ( !res.ok )
        throw Object.assign(new Error(res.statusText + ' ' + url), { res });
      return await res.text();
    },

    addStyle(textContent) {
      const style = Object.assign(document.createElement('style'), { textContent });
      const ref = document.head.getElementsByTagName('style')[0] || null;
      document.head.insertBefore(style, ref);
    },
  }

  const { loadModule } = window['vue3-sfc-loader'];
 
  const app = Vue.createApp({
    components: {
      'mc-main-layout': Vue.defineAsyncComponent( ()=> loadModule('static/components/MainLayout.vue', options)),
      'mc-pokemons': Vue.defineAsyncComponent( () => loadModule('static/components/pokemons.vue', options) )
    }
  });


/*
https://pokeapi.co/api/v2/pokemon?limit=300
https://pokeapi.co/api/v2/pokemon/2/
https://pokeres.bastionbot.org/images/pokemon/2.png

 

*/