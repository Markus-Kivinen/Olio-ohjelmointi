from lib import Menu, SodaBottle


class Main:
    def __init__(self) -> None:
        self.menu: Menu = Menu("Your choice: ")
        self.bottles: list[SodaBottle] = []
        return None

    def start(self) -> None:
        print("Program starting.")
        menu_options = self.menu.get_options()
        menu_text: str = "Menu:\n" + "\n".join(
            f"{key} - {menu_options[key][0]}" for key in menu_options
        )

        while True:
            print(menu_text)
            choice = self.menu.get_input()
            if choice not in menu_options:
                print("Unknown option, try again.\n")
                continue
            menu_func = menu_options[choice][1]
            if not menu_func:
                print(f"'{menu_options[choice][0]}' not implemented yet.\n")
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
