module.exports = {
  devServer: {
    proxy: {
      '^/api/': {
        target: 'http://localhost:8000',
        // logLevel: 'debug',
        changeOrigin: true,
      }
    },
  },
  transpileDependencies: [
    'vuetify'
  ]
}
