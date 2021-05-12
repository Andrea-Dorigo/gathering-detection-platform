// vue.config.js
module.exports = {
  publicPath: "/",
  devServer: {
    port: 8081,
  },
  chainWebpack: (config) => {
    config.module
      .rule("pdf")
      .test(/\.pdf$/)
      .use("file-loader")
      .loader("file-loader");
  },
};
