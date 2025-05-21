
def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    word = get_input("Insert number: ")
    try:
        number = float(word)
        print(f"Inserted value is '{number:.1f}'")
    except ValueError:
        print("Oops! That wasn't valid number.")
    return None


if __name__ == "__main__":
    main()
