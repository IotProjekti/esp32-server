const express = require('express')
const port = process.env.PORT || 3000

const app = express()

app.use(express.json())

let sensorData = []

app.get('/data', (req, res) => {
    res.send(sensorData)
})

app.post('/postdata', (req, res) => {
    let value = req.body.value
    if (sensorData.length < 10) {
        sensorData.push(value)
    } else {
        sensorData.pop()
        sensorData.unshift(value)
    }
    console.log(sensorData)

    res.send(sensorData)
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})