from dataclasses import dataclass
from typing import Callable


@dataclass
class Option:
    name: str
    function: None | Callable[[], None]


class Menu:
    """Menu system for command-line interfaces.

    This class provides functionality for creating and handling
    menu-based interfaces with user options.

    Args:
        - prompt (str): The prompt to display to the user.
        - separator (str): The separator to use between the key and the name
          of the option.
        - options_name (str): The name of the options menu.
    """
    def __init__(self,
                 prompt: str = "Your choice: ",
                 separator: str = " - ",
                 options_name: str = "Options:"
                 ) -> None:
        self.prompt: str = prompt
        self.separator: str = separator
        self.opt_name: str = options_name
        self.options: dict[str, Option] = {}
        self.enabled: bool = False

    def add_option(
        self,
        key: str,
        name: str,
        func: None | Callable[[], None]
    ) -> None:
        """Add an option to the menu.

        Args:
            - key (str): The input the user must input to select the option.
            - name (str): The name of the option.
            - func (None | Callable):
              The function to call when the option is selected.
        """
        self.options[key] = Option(name, func)

    def add_options(
        self,
        options: dict[str, tuple[str, None | Callable[[], None]]]
    ) -> "Menu":
        """Add multiple options to the menu.

        Args:
            - options (dict[str, Tuple[str, | Callable[[], None]]]):
              A dictionary of options to add.
              The key is the input the user must input to select the option,
              and the value is a tuple of the name of the option and the
              function to call when the option is selected.

        Returns:
            - self: The menu object for method chaining.
        """
        for key, (name, func) in options.items():
            self.add_option(key, name, func)

        return self

    def get_option_tree(self) -> str:
        """Get the menu as a string.
        Returns:
            - str: The menu as a string.
        """
        return f"{self.opt_name}\n" + "\n".join(
            f"{key}{self.separator}{self.options[key].name}"
            for key in self.options
        )

    def has_option(self, key: str) -> bool:
        """Check if the menu has an option with the given key.
        Args:
            - key (str): The key to check.
        Returns:
            - bool: True if the menu has an option with the given key,
              False otherwise.
        """
        return key in self.options

    def get_input(self) -> str:
        """Ask the user to select an option.
        Returns:
            - str: The key of the selected option.
        """
        return input(self.prompt)


if __name__ == "__main__":

    def runY():
        print("Y was run\n")

    def exit(menu: Menu):
        print("Exiting...")
        menu.enabled = False

    # menu = Menu("Choose option: ", ": ", "Main menu:")
    # menu.add_option("1", "print X", lambda: print("X\n"))
    # menu.add_option("2", "run Y", runY)
    # menu.add_option("0", "Exit", lambda: exit(menu))
    menu = Menu().add_options(
        {
            "1": ("print X", lambda: print("X\n")),
            "2": ("run Y", runY),
            "0": ("Exit", lambda: exit(menu)),
        }
    )

    def handle_menu(menu: Menu) -> None:
        menu.enabled = True
        while menu.enabled:
            print(menu.get_option_tree())
            user_input = menu.get_input()
            if not menu.has_option(user_input):
                print("Invalid option.")
                continue
            opt = menu.options[user_input]
            if opt.function:
                opt.function()

    handle_menu(menu)
