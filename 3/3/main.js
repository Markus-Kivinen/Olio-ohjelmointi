var Person = /** @class */ (function () {
    function Person(fname, lname, age) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }
    Person.prototype.getAge = function () {
        return this.age;
    };
    Person.prototype.ageUp = function () {
        this.age++;
    };
    Person.prototype.getFullname = function () {
        return this.first_name + " " + this.last_name;
    };
    Person.prototype.printFullName = function () {
        console.log(this.getFullname());
    };
    return Person;
}());
var Main = /** @class */ (function () {
    function Main() {
        console.log("Program starting.");
        console.log("Creating person...");
        var person = new Person("John", "Doe", 30);
        console.log("Person created.");
        console.log("Name:", person.getFullname());
        console.log("Age:", person.getAge());
        console.log("Person has now birthday...");
        person.ageUp();
        console.log("New age:", person.getAge());
        console.log("Program ending.");
    }
    return Main;
}());
var app = new Main();
