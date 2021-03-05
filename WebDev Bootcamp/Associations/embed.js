var mongoose = require("mongoose")

mongoose.set("useNewUrlParser", true)
mongoose.set("useUnifiedTopology", true)
mongoose.connect("mongodb://localhost/blog_demo")

// POST - title, content
var postSchema = new mongoose.Schema({
    title: String,
    content: String,
})

// USER - email, name
var userSchema = new mongoose.Schema({
    name: String,
    email: String,
    posts: [postSchema],
})

var User = mongoose.model("User", userSchema)
var Post = mongoose.model("Post", postSchema)

// var newUser = new User({
//     email: "hermione@hogwarts.edu",
//     name: "Hermione Granger",
// })
// newUser.posts.push({
//     title: "How to brew polyjuice potion",
//     content: "Just kidding, go to potions class!",
// })

// newUser.save((err, user) => {
//     if (err) {
//         console.log(err)
//     } else {
//         console.log(user)
//     }
// })

// var newPost = new Post({
//     title: "Reflections on Apples",
//     content: "They are delicious",
// })

// newPost.save((err, post) => {
//     if (err) {
//         console.log(err)
//     } else {
//         console.log(post)
//     }
// })

User.findOne({ name: "Hermione Granger" }, (err, user) => {
    if (err) {
        console.log(err)
    } else {
        user.posts.push({
            title: "3 things i really hate",
            content: "Voldemort, Voldemort, Voldemort",
        })
        user.save((err, user) => {
            if (err) {
                console.log(err)
            } else {
                console.log(user)
            }
        })
    }
})
