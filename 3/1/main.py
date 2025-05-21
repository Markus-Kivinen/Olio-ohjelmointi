from person import Person


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        print("Creating person...")
        person = Person("John", "Doe", 30)
        print("Person created.")
        print("Name:", person.getFullname())
        print("Age:", person.getAge())
        print("Person has now birthday...")
        person.ageUp()
        print("New age:", person.getAge())
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
