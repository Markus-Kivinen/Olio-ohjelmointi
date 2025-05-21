from pathlib import Path

from .lib import Menu, SodaBottle


class Main:
    def __init__(self) -> None:
        self.menu: Menu = Menu("Your choice: ", " - ")
        self.menu.add_option("1", "Add bottle", self.add_bottle)
        self.menu.add_option("2", "Show bottles", self.list_bottles)
        self.menu.add_option("3", "Save bottle", self.save_bottles)
        self.menu.add_option("0", "Exit", self.exit_app)
        self.bottles: list[SodaBottle] = []
        self.running: bool = False
        return None

    def load_state(self) -> None:
        script_directory = Path(__file__).parent
        in_file = script_directory / "inventory.txt"
        if in_file.exists():
            print("Loading inventory...")
            bottle_strs = in_file.read_text("utf-8").splitlines()
            for bottle_str in bottle_strs:
                bottle = SodaBottle.from_serialized(bottle_str)
                self.bottles.append(bottle)
            print("Inventory loaded.")

    def add_bottle(self) -> None:
        bottle = SodaBottle.from_input()
        self.bottles.append(bottle)
        print("")

    def list_bottles(self) -> None:
        print("#### Soda bottles ####")
        for i in range(len(self.bottles)):
            print(f"Bottle {i+1}:\n" + self.bottles[i].info)
        print("#### Soda bottles ####\n")

    def save_bottles(self) -> None:
        print("Saving soda bottles...")
        output = "\n".join(bottle.serialize() for bottle in self.bottles)
        script_directory = Path(__file__).parent
        out_file = script_directory / "inventory.txt"
        _ = out_file.write_text(output, encoding="utf-8")
        print("Saving completed!\n")

    def start(self) -> None:
        print("Program starting.")
        self.running = True
        self.load_state()
        options = self.menu.options
        option_tree: str = "Menu:\n" + self.menu.get_option_tree()

        while self.running:
            print(option_tree)
            choice = self.menu.get_input()
            if not self.menu.has_option(choice):
                print("Unknown option, try again.\n")
                continue
            menu_func = options[choice].func
            if not menu_func:
                print(f"'{options[choice].name}' not implemented yet.\n")
            else:
                menu_func()
        print("Program ending.")
        return None

    def exit_app(self) -> None:
        print("\nExiting program.")
        self.running = False


if __name__ == "__main__":
    app = Main()
    app.start()
