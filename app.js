const express = require('express')
const port = process.env.PORT || 3000

const app = express()

app.get('/data', (req, res) => {
    res.send(data)
})

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})