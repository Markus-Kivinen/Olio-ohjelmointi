class Person {
    public first_name: string;
    public last_name: string;
    private age: number;
    
    constructor(fname: string, lname: string, age: number){
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    getAge(): number {
        return this.age
    }

    ageUp(): void {
        this.age++;
    }

    getFullname(): string{
        return this.first_name + " " + this.last_name
    }

    printFullName(): void{
        console.log(this.getFullname())
    }
}

class Main{
    constructor() {
        console.log("Program starting.")
        console.log("Creating person...")
        let person = new Person("John", "Doe", 30)
        console.log("Person created.")
        console.log("Name:" + " " + person.getFullname())
        console.log("Age:" + " " + person.getAge())
        console.log("Person has now birthday...")
        person.ageUp()
        console.log("New age:" + " " + person.getAge())
        console.log("Program ending.")
    }
}
let app = new Main()
