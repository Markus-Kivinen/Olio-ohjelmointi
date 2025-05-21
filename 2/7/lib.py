from dataclasses import dataclass
from typing import Callable, Self


@dataclass
class Option:
    name: str
    func: None | Callable[[], None]


class Menu:
    def __init__(self, prompt: str, sep: str) -> None:
        self.prompt: str = prompt
        self.sep: str = sep
        self.options: dict[str, Option] = {}
        return None

    def add_option(
        self,
        key: str,
        name: str,
        func: None | Callable[[], None]
    ) -> None:
        """Add an option to the menu.

        Args:
            - key (str): The string the user must input to select the option.
            - name (str): The name of the option.
            - func (None | Callable):
              The function to call when the option is selected.
        """
        self.options[key] = Option(name, func)

    def get_option_tree(self) -> str:
        return "\n".join(
            f"{key}{self.sep}{self.options[key].name}"
            for key in self.options
        )

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
    def from_serialized(cls, serialized: str) -> Self:
        brand, volume = serialized.split(";")
        return cls(brand, float(volume))

    @classmethod
    def from_input(cls) -> Self:
        print("Creating soda bottle.")
        brand = input("Insert brand: ")
        volume = input("Insert volume: ")
        return cls(brand, float(volume))

    @property
    def info(self) -> str:
        return (f"  brand - {self.brand}\n"
                f"  volume - {self.volume}")
