var path = require("path")
var webpack = require("webpack")

module.exports = {
  context: __dirname,

  entry: {
    chartComponent: './reactjs/chartComponent',
    vendors: ['react'],
  },

  output: {
    path: path.resolve('./static/bundles/local'),
    filename: "[name]-[hash].js"
  },

  externals: [

  ],

  plugins: [
    new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'),
  ],

  module: {
    loaders: []
  },

  resolve: {
    modulesDirectories: ['node_modules', 'bower_components'],
    extensions: ['', '.js', '.jsx']
  },
}