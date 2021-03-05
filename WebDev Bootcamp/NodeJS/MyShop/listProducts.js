var faker = require("faker")

console.log("=====================")
console.log(" WELCOME TO MY SHOP! ")
console.log("=====================")

for (let index = 0; index < 10; index++) {
	console.log(faker.fake("{{commerce.productName}} - ${{commerce.price}}"))
}
