const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
//   outputDir: '../../../deploying_International_compettion/Elearning/docs'
// })

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? '/BrainLending/'  // Use 'BrainLending' as your repository name
    : '/'
}
