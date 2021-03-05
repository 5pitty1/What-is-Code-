var Express = require("express")
var app = Express()

var animalSounds = {
	pig: "Oink",
	cow: "Moo",
	dog: "Woof Woof!"
}

app.get("/", function (req, res) {
	res.send("Hi there, welcome to my assignment")
})

app.get("/speak/:animal", function (req, res) {
	var animal = req.params.animal
	res.send(`The ${animal} says '${animalSounds[animal]}'`)
})

app.get("/repeat/:message/:amount", function (req, res) {
	var message = req.params.message
	var amount = parseInt(req.params.amount)

	var newMessage = ""
	for (let index = 0; index < amount; index++) {
		newMessage += message + " "
	}

	res.send(newMessage)
})

app.get("*", function (req, res) {
	"Sorry, page not found...What are you doing with your life?"
})

app.listen(3000)