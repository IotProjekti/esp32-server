const express = require('express')
const port = process.env.PORT || 3000
const request = require('request');

const app = express()

const url = "https://jsonplaceholder.typicode.com/posts/1";
request.get(url, (error, response, body) => {
    let json = JSON.parse(body);
    console.log(body);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})