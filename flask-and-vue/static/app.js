
const options = {
  moduleCache: {
    vue: Vue
  },

  async getFile(url) {
    const res = await fetch(url);
    console.log(url, res)
    if (!res.ok)
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

const PokemonsList = (resolve) => require(['static/components/PokemonsList.vue'], m => resolve(m.default))
const MainLayout = (resolve) => require(['static/components/PokemonsList.vue'], m => resolve(m.default))

const routes = [
  {
    path: '/',
    component: PokemonsList,
    default: true
  },
]

const router = new VueRouter({
  routes: routes,
  mode: "history",
  base: '/'
});

const app = Vue.createApp({
  router: router,
  components: {
    'mc-main-layout': Vue.defineAsyncComponent(() => loadModule('static/components/MainLayout.vue', options))
  }
})

app.mount('#app')
app.use(router)
console.log('App: ', app)