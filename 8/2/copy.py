import sys
from pathlib import Path


class Main:
    def __init__(self) -> None:
        _, in_file, *out_file = sys.argv

        print(f"Copying {in_file} to {out_file[0]}")
        in_path = Path(in_file)
        out_path = Path(out_file[0])

        content = in_path.read_bytes()
        _ = out_path.write_bytes(content)

        print("Copy operation completed!")
        return None


if __name__ == "__main__":
    main = Main()
