from coin_acceptor import CoinAcceptor


class Main:
    def __init__(self) -> None:
        return None

    def get_choice(self, prompt: str) -> int:
        return int(input(prompt))

    def start(self) -> None:
        print("Program starting.")
        acceptor = CoinAcceptor()
        options = acceptor.get_options()
        options_str = "\n".join(f"{x} - {options[x][0]}" for x in options)

        while True:
            print(options_str)
            choice = self.get_choice("Your choice: ")
            if not choice:
                break
            funktio = options[choice][1]
            _ = funktio()
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
