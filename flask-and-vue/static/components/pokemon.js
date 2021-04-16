const mcPokemon = {
    template: `{{ pokemon.name }} - {{pokemon.url}} `,

    props: {
        pokemon: {
            required: true
        }
    },

    data() {
        return {
            title: 'My title - '
        }
    }
}

app.component('mc-pokemon', mcPokemon)

