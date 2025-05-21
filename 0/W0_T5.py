
def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    summed = 0
    print(f"Current value {summed:.1f}")
    while word := get_input("Add number(empty stops): "):
        summed += float(word)
        print(f"Current value {summed:.1f}")
    print(f"Final value {summed:.1f}")
    return None


if __name__ == "__main__":
    main()
