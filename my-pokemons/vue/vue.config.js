module.exports = {
    filenameHashing: false,
    configureWebpack: config => {
      config.optimization.splitChunks = false
    }
  }