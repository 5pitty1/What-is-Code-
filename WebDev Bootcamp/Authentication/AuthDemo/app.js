var express = require("express")
var mongoose = require("mongoose")
var passport = require("passport")
var bodyParser = require("body-parser")
var LocalStrategy = require("passport-local")
var passportLocalMongoose = require("passport-local-mongoose")
var expressSession = require("express-session")
var User = require("./models/user")

// Database Setup - Mongoose deprecation settings, mongoose local host
mongoose.set("useNewUrlParser", true)
mongoose.set("useUnifiedTopology", true)
mongoose.connect("mongodb://localhost/auth_demo_app")

// Express Setup - ejs engine, passport, session secret
var app = express()
app.set("view engine", "ejs")
app.use(bodyParser.urlencoded({ extended: true }))
app.use(
    expressSession({
        secret: "pokemon is the best video game!!!",
        resave: false,
        saveUninitialized: false,
    })
)
app.use(passport.initialize())
app.use(passport.session())

// Passport Setup - serializing data
passport.use(new LocalStrategy(User.authenticate()))
passport.serializeUser(User.serializeUser())
passport.deserializeUser(User.deserializeUser())

// Middleware
function isLoggedIn(req, res, next) {
    console.log(req.isAuthenticated())
    if (req.isAuthenticated()) {
        return next()
    }

    res.redirect("/login")
}

// Routes
app.get("/", (req, res) => {
    res.render("home")
})

app.get("/secret", isLoggedIn, (req, res) => {
    res.render("secret")
})

app.get("/register", (req, res) => {
    res.render("register")
})

app.post("/register", async (req, res) => {
    try {
        let user = await User.register(
            new User({ username: req.body.username }),
            req.body.password
        )
        passport.authenticate("local")(req, res, () => {
            res.redirect("/secret")
        })
    } catch (error) {
        console.log(error)
        return res.render("register")
    }
})

app.get("/login", (req, res) => {
    res.render("login")
})

app.post(
    "/login",
    passport.authenticate("local", {
        successRedirect: "/secret",
        failureRedirect: "/login",
    }),
    (req, res) => {}
)

app.get("/logout", (req, res) => {
    req.logout()
    res.redirect("/")
})

app.listen(3000, () => {
    console.log("server started.....")
})
