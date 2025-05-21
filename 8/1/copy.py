from pathlib import Path


class Main:
    def __init__(self) -> None:
        print("Welcome to the copy utility.")

        in_path = Path(input("Insert source filepath: "))
        out_path = Path(input("Insert destination filepath: "))

        content = in_path.read_bytes()
        _ = out_path.write_bytes(content)

        print("Copy operation completed!")
        return None


if __name__ == "__main__":
    main = Main()
