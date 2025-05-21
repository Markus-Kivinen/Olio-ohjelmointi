import sys

CHAR_ALPHA: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
CHAR_ROT: str = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"


class Main:
    def __init__(self) -> None:
        _, *uncrypted = sys.argv

        crypted: list[str] = []
        for c in " ".join(uncrypted):
            try:
                num = (int(c) + 5) % 10
                crypted.append(str(num))
            except ValueError:
                try:
                    index = CHAR_ALPHA.index(c)
                    crypted.append(CHAR_ROT[index])
                except ValueError:
                    crypted.append(c)

        output = "".join(crypted)
        print(f"{output}")
        return None


if __name__ == "__main__":
    main = Main()
