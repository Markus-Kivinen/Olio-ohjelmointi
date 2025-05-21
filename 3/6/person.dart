class Person {
    String first_name;
    String last_name;
    int _age;
    
    Person(this.first_name, this.last_name, this._age);

    int getAge() {
        return _age;
    }

    void ageUp(){
        _age += 1;
    }

    String getFullname(){
        return '$first_name $last_name';
    }

    void printFullName(){
        print(getFullname());
    }
}