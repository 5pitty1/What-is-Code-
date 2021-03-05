var Express = require("express")
var app = Express()

app.use(Express.static("public"))
app.set("view engine", "ejs")


app.get("/", function (req, res) {
	res.render("home")
})

app.get("/fallinlovewith/:thing", function (req, res) {
	var thing = req.params.thing

	res.render("love", {
		thingVar: thing
	})
})

app.get("/posts", function (req, res) {
	var posts = [
		{ title: "Post 1", author: "Susy" },
		{ title: "I have a cute cat!", author: "Andy" },
		{ title: "I am magic ;)", author: "Mike" }
	]

	res.render("posts", {
		posts: posts
	})
})

app.listen(3000, function () {
	console.log("Server is listening!!!")
})