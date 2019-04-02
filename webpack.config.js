var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: 'development',
  context: __dirname,
  entry: './assets/js/index.ts',
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
  ],

  module: {
    rules: [
      {
        test: /.ts$/, use: 'ts-loader'
      }
    ]
  },


  resolve: {
    extensions: ['.js', '.jsx']
  },
}