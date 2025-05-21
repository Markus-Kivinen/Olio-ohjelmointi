#include <iostream>
#include "person.h"

int main() {
    std::cout << "Program starting." << std::endl;
    std::cout << "Creating person..." << std::endl;
    Person person("John", "Doe", 30);
    std::cout << "Person created." << std::endl;
    std::cout << "Name: " << person.getFullname() << std::endl;
    std::cout << "Age: " << person.getAge() << std::endl;
    std::cout << "Person has now birthday..." << std::endl;
    person.ageUp();
    std::cout << "New age: " << person.getAge() << std::endl;
    std::cout << "Program ending." << std::endl;

    return 0;
}