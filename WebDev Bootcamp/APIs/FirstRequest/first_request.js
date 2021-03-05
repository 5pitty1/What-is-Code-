const axios = require("axios")
const locus = require("locus")

axios.get('https://jsonplaceholder.typicode.com/todos/1')
	.then((response) => {
		eval(locus)
		console.log(response.data)
	})
	.catch((error) => {
		console.log(error)

	})
	.finally(() => {

	})