class Person{
    /** @type {string} */
    first_name;
    /** @type {string} */
    last_name;
    /** @type {number} */
    #age;
    
    constructor(fname, lname, age){
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    /** @returns {number} */
    getAge() {
        return this.age
    }

    ageUp(){
        this.age++;
    }

    /** @returns {string} */
    getFullname(){
        return `${this.first_name} ${this.last_name}`
    }

    printFullName(){
        console.log(this.getFullname())
    }
}

module.exports = Person