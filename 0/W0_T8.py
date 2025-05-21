from math import pi, tau


def main() -> None:
    if pi == tau:
        print("Tau equals Pi.")
    else:
        print("Tau doesn't equal Pi.")
    if pi * 2 == tau:
        print("Tau equals 2 * Pi.")
    else:
        print("Tau doesn't equal 2 * Pi.")
    return None


if __name__ == "__main__":
    main()
