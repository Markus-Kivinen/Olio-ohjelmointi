from typing import Callable, Optional


class CoinAcceptor:
    def __init__(self) -> None:
        self.__count = 0
        self.__value = 0
        return None

    def get_options(
        self
    ) -> dict[int, tuple[str, Callable[[], None | int]]]:
        return {
            1: ("Insert coin", self.insertCoin),
            2: ("Show coins", self.getAmount),
            3: ("Return coins", self.returnCoins),
            0: ("Exit program", lambda: None),
        }

    def insertCoin(self) -> None:
        self.__count += 1
        return None

    def getAmount(self) -> int:
        print(f"Currently '{self.__count}' coins in coin acceptor")
        return self.__count

    def returnCoins(self) -> int:
        count, self.__count = self.__count, 0
        print(f"Coin acceptor returned '{count}' coins.")
        return count
