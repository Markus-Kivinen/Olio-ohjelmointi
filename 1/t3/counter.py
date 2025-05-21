from typing import Callable


class Counter:
    def __init__(self) -> None:
        self.__count = 0
        return None

    def get_options(
        self
    ) -> dict[int, tuple[str, Callable[[], None | int]]]:
        return {
            1: ("Add count", self.addCount),
            2: ("Get count", self.getCount),
            3: ("Zero count", self.zeroCount),
            0: ("Exit program", self.quit),
        }

    def addCount(self) -> None:
        self.__count += 1
        print("Count increased")
        return None

    def getCount(self) -> int:
        print(f"Current count '{self.__count}'")
        return self.__count

    def zeroCount(self) -> None:
        self.__count = 0
        print("Count zeroed")
        return None

    def quit(self) -> None:
        pass
