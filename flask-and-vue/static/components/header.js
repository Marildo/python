const MyHeader = {
    template: `<h2>Eu sou o o header: {{ title + subtitle}}</h2>`,

    props: {
        subtitle: {
            type: String,
            default: 'Não informado',
            required: false
        }
    },

    data() {
        return {
            title: 'My title - '
        }
    }
}

app.component('my-header', MyHeader)