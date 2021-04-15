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
        reverseMessage() {
            this.message = this.message
                .split('')
                .reverse()
                .join('')
        }
    }
}

const app = Vue.createApp(HelloVueApp)
