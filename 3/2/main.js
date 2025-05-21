const Person = require('./person')


class Main{
    constructor() {
        console.log("Program starting.")
        console.log("Creating person...")
        let person = new Person("John", "Doe", 30)
        console.log("Person created.")
        console.log("Name:", person.getFullname())
        console.log("Age:", person.getAge())
        console.log("Person has now birthday...")
        person.ageUp()
        console.log("New age:", person.getAge())
        console.log("Program ending.")
    }
}
let app = new Main()
