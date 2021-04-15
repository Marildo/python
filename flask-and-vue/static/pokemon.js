const mcPokemon = {
    template: `{{ pokemon }}`,

    props: {
        pokemon: {
            type: String,
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