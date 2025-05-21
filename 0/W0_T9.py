from pathlib import Path

ROOT_FOLDER = Path(__file__).parent


def get_input(prompt: str) -> str:
    return input(prompt)


def main() -> None:
    filename = get_input("Insert filename to read: ")
    file_path = ROOT_FOLDER / filename
    if file_path.exists():
        print(f"#### {filename} content ####")
        print(file_path.read_text())
        print(f"#### {filename} content ####")
    else:
        print(f"File '{filename}' not found.")
    return None


if __name__ == "__main__":
    main()
