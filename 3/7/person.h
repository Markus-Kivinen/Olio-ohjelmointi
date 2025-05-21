#include <string>
#include <iostream>

class Person {
public:
    Person(const std::string& fname, const std::string& lname, int age)
        : first_name(fname), last_name(lname), age(age) {}

    int getAge() const {
        return age;
    }

    void ageUp() {
        age++;
    }

    std::string getFullname() const {
        return first_name + " " + last_name;
    }

    void printFullName() const {
        std::cout << getFullname() << std::endl;
    }

public:
    std::string first_name;
    std::string last_name;

private:
    int age;
};