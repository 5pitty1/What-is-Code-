var express = require("express")
var axios = require("axios")

app = express()
app.set("view engine", "ejs")

app.get("/", (req, res) => {
	res.render("search")
})

app.get("/results", (req, res) => {
	var query = req.query.search
	var url = `http://www.omdbapi.com/?apikey=thewdb&s=${query}`
	axios.get(url)
		.then((response) => {
			res.render("results", {
				data: response.data
			})
		})
		.catch((error) => {
			console.log(error)
		})
})

app.listen(3000, () => {
	console.log("Movie app has started!")
})