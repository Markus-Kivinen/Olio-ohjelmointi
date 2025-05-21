from pathlib import Path

ROOT_FOLDER = Path(__file__).parent


def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    haystack = get_input("Insert word: ")
    needle = get_input("Insert search term: ")
    if needle in haystack:
        print(f"Search term '{needle}' do appear in word '{haystack}'")
    else:
        print(f"Search term '{needle}' doesn't appears in word '{haystack}'")
    return None


if __name__ == "__main__":
    main()
