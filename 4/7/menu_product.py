from dataclasses import dataclass
from typing import Callable


@dataclass
class Option:
    name: str
    func: None | Callable[[], None]


class MenuProduct:
    def __init__(self, prompt: str = "Your choice: ", sep: str = " - ") -> None:
        self.prompt: str = prompt
        self.sep: str = sep
        self.options: dict[int, Option] = {}
        return None

    def add_option(
        self,
        key: int,
        name: str,
        func: None | Callable[[], None]
    ) -> None:
        """Add an option to the menu.

        Args:
            - key (int): The number the user must input to select the option.
            - name (str): The name of the option.
            - func (None | Callable):
              The function to call when the option is selected.
        """
        self.options[key] = Option(name, func)

    def get_option_tree(self) -> str:
        return "Options:\n" + "\n".join(
            f"{key}{self.sep}{self.options[key].name}"
            for key in self.options
        )

    def showOptions(self) -> None:
        print(self.get_option_tree())

    def has_option(self, key: int) -> bool:
        return key in self.options

    def askChoice(self) -> int:
        return int(input(self.prompt))
