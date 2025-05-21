from dataclasses import dataclass
from typing import Self, Callable


class Menu:
    def __init__(self, prompt: str) -> None:
        self.prompt: str = prompt
        return None

    def get_options(self) -> dict[
        str,
        tuple[str,
              None | Callable[[], None]]]:
        return {
            "1": ("Add bottle", None),
            "2": ("Show bottle", None),
            "3": ("Save bottle", None),
            "0": ("Exit", self.exit_menu),
        }

    def exit_menu(self) -> None:
        pass

    def get_input(self) -> str:
        return input(self.prompt)


@dataclass
class SodaBottle:
    brand: str
    volume: float

    def serialize(self) -> str:
        return f"{self.brand};{round(self.volume, 2)}"

    @classmethod
    def deserialize(cls, serialized: str) -> Self:
        brand, volume = serialized.split(";")
        return cls(brand, float(volume))
