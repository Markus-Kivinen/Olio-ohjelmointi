from coin_acceptor import CoinAcceptor


class Main:
    def __init__(self) -> None:
        return None

    def get_choice(self, prompt: str) -> str:
        return input(prompt)

    def start(self) -> None:
        print("Program starting.")
        print("Welcome to coin acceptor program.")
        print("Insert new coin by typing it's value (0 returns the money, " +
              "-1 exits the program)")
        acceptor = CoinAcceptor()

        prompt = "\nInsert coin(0 return, -1 exit): "
        while (choice := self.get_choice(prompt)) != "-1":
            if choice == "0":
                coins, value = acceptor.returnCoins()
                print(f"{coins} coins with {value:.1f}€ value returned.")
                print(repr(acceptor))
            else:
                acceptor.insertCoin(float(choice))
                print(repr(acceptor))
        print("Exiting program.\n\nProgram ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
