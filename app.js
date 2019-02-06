const express = require('express')
const hbs = require('hbs')
const port = process.env.PORT || 3000

const app = express()

app.set('view engine', 'hbs')
app.use(express.json())


let sensorData = [100, 200, 300]


app.get('/', (req, res) => {
    res.render('trafficlight.hbs', {
        value: sensorData[0]
    })
})

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