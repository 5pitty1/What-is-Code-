var mongoose = require("mongoose")

mongoose.set("useNewUrlParser", true)
mongoose.set("useUnifiedTopology", true)
mongoose.connect("mongodb://localhost/blog_demo_2")

var Post = require("./models/post")
var User = require("./models/user")

// User.create({
//     email: "bob@gmail.com",
//     name: "Bob Belcher",
// })

Post.create(
    {
        title: "How to cook the best burger (Part 4)",
        content: "fjdkslfsd",
    },
    (err, post) => {
        User.findOne({ email: "bob@gmail.com" }, (err, foundUser) => {
            if (err) {
                console.log(err)
            } else {
                foundUser.posts.push(post)
                foundUser.save((err, data) => {
                    if (err) {
                        console.log(err)
                    } else {
                        console.log(data)
                    }
                })
            }
        })
    }
)

// Find User
// Find all posts for that user

// User.findOne({ email: "bob@gmail.com" })
//     .populate("posts")
//     .exec((err, user) => {
//         if (err) {
//             console.log(err)
//         } else {
//             console.log(user)
//         }
//     })
