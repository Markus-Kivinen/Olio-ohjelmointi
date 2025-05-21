from pathlib import Path
from lib import Menu, SodaBottle


class Main:
    def __init__(self) -> None:
        self.menu: Menu = Menu("Your choice: ")
        self.menu.add_option("1", "Add bottle", self.add_bottle)
        self.menu.add_option("2", "Show bottles", self.list_bottles)
        self.menu.add_option("3", "Save bottle", self.save_bottles)
        self.menu.add_option("0", "Exit", self.exit_menu)
        self.bottles: list[SodaBottle] = []
        return None

    def add_bottle(self) -> None:
        bottle = SodaBottle.from_input()
        self.bottles.append(bottle)

    def save_bottles(self) -> None:
        print("Saving soda bottles...")
        output = "\n".join(bottle.serialize() for bottle in self.bottles)
        script_directory = Path(__file__).parent
        out_file = script_directory / "inventory.txt"
        _ = out_file.write_text(output, encoding="utf-8")
        print("Saving completed!")

    def list_bottles(self) -> None:
        print("#### Soda bottles ####")
        for i in range(len(self.bottles)):
            print(f"Bottle {i+1}:\n" + (self.bottles[i].info))
        print("#### Soda bottles ####")

    def exit_menu(self) -> None:
        pass

    def start(self) -> None:
        print("Program starting.")
        options = self.menu.options
        options_str: str = "Menu:\n" + "\n".join(
            f"{key} - {options[key][0]}" for key in options
        )

        while True:
            print(options_str)
            choice = self.menu.get_input()
            if not self.menu.has_option(choice):
                print("Unknown option, try again.\n")
                continue
            menu_func = options[choice][1]
            if not menu_func:
                print(f"'{options[choice][0]}' not implemented yet.\n")
            else:
                _ = menu_func()
                print("")
                if choice == "0":
                    print("Exiting program.")
                    break
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
