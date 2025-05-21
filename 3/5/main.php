<?php
class Person {
    public $first_name;
    public $last_name;
    private $age;
    
    public function __construct($fname, $lname, $age){
        $this->first_name = $fname;
        $this->last_name = $lname;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp(){
        $this->age++;
    }

    public function getFullname(){
        return $this->first_name . " " . $this->last_name;
    }

    public function printFullName(){
        echo $this->getFullname() . "\n";
    }
}
class Main{
    public function __construct() {
        echo "Program starting.\n";
        echo "Creating person...\n";
        $person = new Person("John", "Doe", 30);
        echo "Person created.\n";
        echo "Name: ", $person->getFullname() . "\n";
        echo "Age: ", $person->getAge() . "\n";
        echo "Person has now birthday...\n";
        $person->ageUp();
        echo "New age: ", $person->getAge() . "\n";
        echo "Program ending.\n";
    }
}
$main = new Main();
?>