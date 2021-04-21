export default {
    loadImage(image) {
        const path = process.env.NODE_ENV === 'production' ? 'dist/' : ''
        return `/${path.trim()}img/${image}`
    }
};
