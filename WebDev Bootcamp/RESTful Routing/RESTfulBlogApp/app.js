var express = require("express")
var bodyParser = require("body-parser")
var mongoose = require("mongoose")
var methodOverride = require("method-override")
var expressSanitizer = require("express-sanitizer")

// Mongoose Config
mongoose.set("useNewUrlParser", true)
mongoose.set("useUnifiedTopology", true)
mongoose.connect("mongodb://localhost/restful_blog_app")

// App Config
var app = express()
app.set("view engine", "ejs")
app.use(express.static("public"))
app.use(bodyParser.urlencoded({ extended: true }))
app.use(methodOverride("_method"))
app.use(expressSanitizer())

// MONGOOSE/MODEL CONFIG
var blogSchema = new mongoose.Schema({
    title: String,
    image: String,
    body: String,
    created: { type: Date, default: Date.now() },
})

var Blog = mongoose.model("Blog", blogSchema)

// Index route
app.get("/", (req, res) => {
    res.redirect("/blogs")
})

app.get("/blogs", (req, res) => {
    Blog.find({}, (err, blogs) => {
        if (err) {
            console.log(err)
        } else {
            res.render("index", { blogs: blogs })
        }
    })
})

// New route
app.get("/blogs/new", (req, res) => {
    res.render("new")
})

// Create route
app.post("/blogs", (req, res) => {
    var blog = req.body.blog
    blog.body = req.sanitize(blog.body)

    Blog.create(blog, (err, newBlog) => {
        if (err) {
            res.render("new")
        } else {
            res.redirect("/blogs")
        }
    })
})

// Show route
app.get("/blogs/:id", (req, res) => {
    Blog.findById(req.params.id, (err, foundBlog) => {
        if (err) {
            res.redirect("/blogs")
        } else {
            res.render("show", { blog: foundBlog })
        }
    })
})

// Edit route
app.get("/blogs/:id/edit", (req, res) => {
    Blog.findById(req.params.id, (err, foundBlog) => {
        if (err) {
            res.redirect("/blogs")
        }
        res.render("edit", { blog: foundBlog })
    })
})

// Update Route
app.put("/blogs/:id", (req, res) => {
    var blog = req.body.blog
    blog.body = req.sanitize(blog.body)

    Blog.findByIdAndUpdate(req.params.id, req.body.blog, (err, updatedBlog) => {
        if (err) {
            res.redirect("/blogs")
        } else {
            res.redirect(`/blogs/${req.params.id}`)
        }
    })
})

// Delete route
app.delete("/blogs/:id", (req, res) => {
    Blog.findByIdAndDelete(req.params.id, req.body.blog, (err) => {
        if (err) {
            res.redirect("/blogs")
        } else {
            res.redirect("/blogs")
        }
    })
})

app.listen(3000, () => {
    console.log("Server is running!")
})
