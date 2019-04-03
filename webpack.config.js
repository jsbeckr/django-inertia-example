const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

const glob = require("glob-all");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const PurgecssPlugin = require("purgecss-webpack-plugin");

class TailwindExtractor {
  static extract(content) {
    return content.match(/[A-Za-z0-9-_:\/]+/g) || [];
  }
}

module.exports = {
  mode: 'development',
  devtool: 'inline-source-map',
  context: __dirname,
  entry: ["./assets/js/index.js", "./assets/css/index.postcss"],
  output: {
    publicPath: "/static/bundles/",
    filename: "[name]-[hash].js",
    chunkFilename: '[name]-[hash].js',
    path: path.resolve('./assets/bundles/'),
  },

  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
    new VueLoaderPlugin(),
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: "[name]-[hash].css"
    }),
    new PurgecssPlugin({
      paths: glob.sync([
        path.join(__dirname, "assets/js/**/*.vue"),
        path.join(__dirname, "core/templates/index.html")
      ]),
      extractors: [
        {
          extractor: TailwindExtractor,
          extensions: ["html", "js", "vue"]
        }
      ]
    })
  ],

  module: {
    rules: [
      {
        test: /\.m?js$/,
        exclude: /(node_modules|bower_components)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [
              '@babel/preset-env'
            ],
            plugins: ["@babel/plugin-syntax-dynamic-import"]
          }
        }
      },
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.postcss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          { loader: 'css-loader', options: { importLoaders: 1 } },
          'postcss-loader',
        
        ]
      }
    ]
  },

  resolve: {
    extensions: ['.js'],
    alias: {
      'vue$': 'vue/dist/vue.runtime.js',
      '@': path.resolve('assets/js'),
    }
  },
}