const path = require('path');

module.exports = {
    entry: './assets/index.js',
    output: {
        chunkFilename: "[name].bundle.js",
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'static')
    },
    module: {
        rules: [
            {
                test: /\.(s*)css$/,
                exclude: /node_modules/,
                use: [
                    {loader: 'style-loader'},
                    {loader: 'css-loader', options: {sourceMap: true}},
                    {loader: 'sass-loader', options: {sourceMap: true}},
                ]
            },
            {
                test: /\.(png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot)(\?.*$|$)/,
                use: [
                    {loader: 'file-loader'}
                ]
            }
        ]
    }
};