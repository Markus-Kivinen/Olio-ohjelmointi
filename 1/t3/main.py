from counter import Counter


class Main:
    def __init__(self) -> None:
        return None

    def get_choice(self, prompt: str) -> int:
        return int(input(prompt))

    def start(self) -> None:
        print("Program starting.")
        print("Initializing counter...")
        counter = Counter()
        print("Counter initialized.")

        options = counter.get_options()
        options_str = ("\nOptions:\n"
                       + "\n".join(f"{x}) {options[x][0]}" for x in options))
        while True:
            print(options_str)
            choice = self.get_choice("Choice: ")
            if not choice:
                break
            _ = options[choice][1]()
        print("\nProgram ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
