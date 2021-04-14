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

Vue.createApp(HelloVueApp).mount('#app')