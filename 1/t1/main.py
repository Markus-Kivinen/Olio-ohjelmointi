from person import Person


def main() -> None:
    print("Program starting.")
    print("Initializing persons...")
    jane = Person("Jane", "Morgan")
    johnn = Person("John", "Doe")
    print("Persons initialized, names below.")
    jane.fullname()
    johnn.fullname()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
