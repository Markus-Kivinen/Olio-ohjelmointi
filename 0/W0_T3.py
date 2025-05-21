
def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    word = get_input("Insert age: ")
    age = int(word)
    if age >= 18:
        print("Adult")
    else:
        print("Child")
    return None


if __name__ == "__main__":
    main()
