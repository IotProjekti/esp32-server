const express = require('express')
const hbs = require('hbs')
const path = require('path')
const port = process.env.PORT || 3006

const app = express()

app.set('view engine', 'hbs')
app.use(express.json())
app.use(express.static(path.join(__dirname + '/public')))

let sensorData = [100, 200, 300, 20]
let red = false
let yellow = false
let green = false

app.get('/', (req, res) => {
    let currValue = sensorData[sensorData.length - 1]
    if (currValue < 100) {
        res.render('trafficlight.hbs', {
            green: true,
            value: currValue.toString()
        })
    } else if (currValue >= 100 && currValue < 200) {
        res.render('trafficlight.hbs', {
            yellow: true,
            value: currValue.toString()
        })
    } else {
        res.render('trafficlight.hbs', {
            red: true,
            value: currValue.toString()
        })
    }
})

app.get('/data', (req, res) => {
    res.send(sensorData)
})

app.post('/postdata', (req, res) => {
    let value = req.body.value
    let value1 = req.body.value1
    let value2 = req.body.value2
    if (sensorData.length < 10) {
        sensorData.push(value)
        sensorData.push(value1)
        sensorData.push(value2)
    } else {
        sensorData.pop()
        sensorData.unshift(value)
        sensorData.unshift(value1)
        sensorData.unshift(value2)
    }
    console.log(sensorData)

    res.send(sensorData)
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Example app listening on port ${port}`)
})