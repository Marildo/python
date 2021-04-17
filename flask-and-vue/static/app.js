const options = {
    moduleCache: {
      vue: Vue
    },

    async getFile(url) {
      const res = await fetch(url);
      console.log(url, res)  
      if ( !res.ok )
        console.error(new Error(res.statusText + ' ' + url), { res });
      return await res.text();
    },

    addStyle(textContent) {
      const style = Object.assign(document.createElement('style'), { textContent });
      const ref = document.head.getElementsByTagName('style')[0] || null;
      document.head.insertBefore(style, ref)
    },
  }

  const { loadModule } = window['vue3-sfc-loader'];
 
  const app = Vue.createApp({
    components: {
      'mc-main-layout': Vue.defineAsyncComponent( ()=> loadModule('static/components/MainLayout.vue', options))
    }
  })

  app.mount('#app')

/*
https://pokeapi.co/api/v2/pokemon?limit=300
https://pokeapi.co/api/v2/pokemon/2/
https://pokeres.bastionbot.org/images/pokemon/2.png


*/