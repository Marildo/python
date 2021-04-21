const isProduction = process.env.NODE_ENV === 'production'

module.exports = {
  filenameHashing: false,
  configureWebpack: config => {
    config.optimization.splitChunks = false
  },

  chainWebpack: (config) => {
    config.module
      .rule("images")
      .use("url-loader")
      .tap((options) => {
        options.name = "images/[name].[ext]";
        options.publicPath = isProduction ? 'dist/' : '/';
        return options;
      });
  },
}