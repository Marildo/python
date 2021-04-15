const HelloVueApp = {
    delimiters: ['[[', ']]'],

    data() {
        return {
            message: 'Hello Vue!!'
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

const MyHeader = {
    template: `<h2>Eu sou o o header: {{ title + subtitle}}</h2>`,

    props: ['subtitle'],

    data() {
        return {
            title: 'My title - '
        }
    }
}

const app = Vue.createApp(HelloVueApp)

app.component('my-header', MyHeader)

app.mount('#app')