from car import Car


class Main:
    def __init__(self) -> None:
        return None

    def start(self) -> None:
        print("Program starting.")
        print("Initializing three car objects.")
        red_car = Car("red")
        green_car = Car("green")
        blue_car = Car("blue")
        print("Car objects initialized.")
        print("Starting the first car object.")
        red_car.start()
        print("Starting the second car object.")
        green_car.start()
        print("Starting the third car object.")
        blue_car.start()
        print("Starting the third car object.")
        blue_car.start()
        print("Program ending.")
        return None


if __name__ == "__main__":
    app = Main()
    app.start()
