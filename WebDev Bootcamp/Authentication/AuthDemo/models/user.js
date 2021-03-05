var mongoose = require("mongoose")
var passportLocalMongoose = require("passport-local-mongoose")

UserSchema = mongoose.Schema({
    username: String,
    password: String,
})

UserSchema.plugin(passportLocalMongoose)

module.exports = mongoose.model("user", UserSchema)
