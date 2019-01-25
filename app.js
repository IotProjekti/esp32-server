const express = require('express')
const port = process.env.PORT || 3000

const app = express()

app.use(express.json())

let sensorData = [{
    id: 1,
    message: 'Hello from Node'
}]

app.get('/data', (req, res) => {
    res.send(sensorData)
})

app.post('/postdata', (req, res) => {
    let data = {
        id: sensorData.length + 1,
        message: req.body.message
    }
    console.log(req.body)
    sensorData.push(data)
    res.send(data)
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})