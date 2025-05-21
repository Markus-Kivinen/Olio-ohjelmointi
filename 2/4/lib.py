from dataclasses import dataclass
from typing import Callable, Self


class Menu:
    def __init__(self, prompt: str) -> None:
        self.prompt: str = prompt
        self.options: dict[str, tuple[str, None | Callable[[], None]]] = {}
        return None

    def add_option(
        self, user_input: str, name: str, func: None | Callable[[], None]
    ) -> None:
        self.options[user_input] = (name, func)

    def has_option(self, key: str) -> bool:
        return key in self.options

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

    @classmethod
    def from_input(cls) -> Self:
        print("Creating soda bottle.")
        brand = input("Insert brand: ")
        volume = input("Insert volume: ")
        return cls(brand, float(volume))

    def __repr__(self) -> str:
        return (f"  brand - {self.brand}\n"
                f"  volume - {self.volume}")
