from lib import SodaBottle


class Main:
    def __init__(self) -> None:
        return None

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def start(self) -> None:
        print("Program starting.")
        print("Constructing soda bottle.")
        brand = self.get_input("Insert brand: ")
        volume = float(self.get_input("Insert volume: "))
        bottle = SodaBottle(brand, volume)
        print("SodaBottle object created!")
        print("Serializing SodaBottle object.")
        serialized = bottle.serialize()
        print("Serialized sodabottle:")
        print(serialized)
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
