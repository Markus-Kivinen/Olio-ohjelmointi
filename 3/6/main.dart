import 'person.dart';

class Main{
    Main() {
        print("Program starting.");
        print("Creating person...");
        var person = Person("John", "Doe", 30);
        print("Person created.");
        print("Name: ${person.getFullname()}");
        print("Age: ${person.getAge()}");
        print("Person has now birthday...");
        person.ageUp();
        print("New age: ${person.getAge()}");
        print("Program ending.");
    }
}
void main() {
    Main();
}