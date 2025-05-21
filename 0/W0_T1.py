
def get_name() -> str:
    return input("Insert name: ")


def main() -> None:
    name = get_name()
    print(f"Hello {name}")
    return None


if __name__ == "__main__":
    main()
