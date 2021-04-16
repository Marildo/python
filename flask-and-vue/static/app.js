const HelloVueApp = {
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
        },

        loadPokemons(){
            axios.get(`https://pokeapi.co/api/v2/ability/38/`)
						.then(response => {
							console.log(response.data)
						})
        }
    }
}

const app = Vue.createApp(HelloVueApp)
