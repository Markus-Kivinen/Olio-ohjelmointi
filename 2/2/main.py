from lib import SodaBottle
from pathlib import Path


class Main:
    def __init__(self) -> None:
        return None

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def start(self) -> None:
        print("Program starting.")
        filename = self.get_input("Insert filename: ")
        filepath = Path(__file__).parent / filename
        serialized = filepath.read_text("utf-8").strip()
        print(f'Deserializing "{serialized}"')
        bottle = SodaBottle.deserialize(serialized)
        print(f"Looks like {bottle.volume:.1f} litre {bottle.brand} bottle.")
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
