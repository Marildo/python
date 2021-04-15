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

const app = Vue.createApp(HelloVueApp)
