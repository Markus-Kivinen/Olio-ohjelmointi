
def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    print("Per Miller's Law, humans can retain ~7 items in short-term memory.")
    word = get_input("Insert memorable string: ")
    if len(word) < 7:
        print("This string will be easy to remember.")
    else:
        print("This string will be hard to remember.")
    return None


if __name__ == "__main__":
    main()
