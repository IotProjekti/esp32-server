const express = require('express')
const port = process.env.PORT || 3000

const app = express()

app.get('/data', (req, res) => {
    res.send(data)
})

app.post('/postdata', (req, res) => {
	let data = req.body.data; // your data
    // do something with that data (write to a DB, for instance)
	res.status(200).json({
		message: "Data received successfully"
	});
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`)
})