from dataclasses import dataclass


@dataclass
class Car:
    color: str
    engine_on: bool = False

    def start(self) -> None:
        if self.engine_on:
            print(f"{self.color} is already running.")
        else:
            print(f"{self.color} car started.")
            self.engine_on = True
        return None
