var mongoose = require("mongoose")

// Load up mongoose server
mongoose.set("useNewUrlParser", true)
mongoose.set("useUnifiedTopology", true)
mongoose.connect("mongodb://localhost/cat_app")

var catSchema = new mongoose.Schema({
    name: String,
    age: Number,
    temperament: String,
})

var Cat = mongoose.model("Cat", catSchema)

// var george = new Cat({
//     name: "Mrs. Norris",
//     age: 7,
//     temperament: "Evil",
// })

// george.save((err, cat) => {
// 	if (err) {
// 		console.log("SOMETHING WENT WRONG!!!")
// 	} else {
// 		console.log("We just saved a cat to the db:")
// 		console.log(cat)
// 	}
// })

// Cat.find({}, (err, cats) => {
//     if (err) {
//         console.log("Oh no!")
//         console.log(err)
//     } else {
//         console.log("All the cats:")
//         console.log(cats)
//     }
// })

Cat.create(
    {
        name: "Snow White",
        age: 15,
        temperament: "Bland",
    },
    (err, cat) => {
        if (err) {
            console.log(err)
        } else {
            console.log(cat)
        }
    }
)
