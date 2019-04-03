const nesting = require('postcss-nesting');
const tailwind = require('tailwindcss');
const autoprefixer = require('autoprefixer');

module.exports = {
  plugins: [
    tailwind('./tailwind.js'),
    nesting(),
    autoprefixer()
  ],
  sourceMap: true
}