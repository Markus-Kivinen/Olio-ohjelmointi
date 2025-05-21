from dataclasses import dataclass


@dataclass
class CoinAcceptor:
    _count: int = 0
    _value: float = 0

    def insertCoin(self, value: float) -> None:
        print("Inserting...")
        self._count += 1
        self._value += value
        return None

    def getAmount(self) -> int:
        print(f"Currently '{self._count}' coins in coin acceptor")
        return self._count

    def returnCoins(self) -> tuple[int, float]:
        print("Returning coins...")
        count, value = self._count, self._value
        self._count, self._value = 0, 0
        return count, value

    def __repr__(self) -> str:
        return (
            f"Inserted coins - {self._count}, "
            f"value - {round(self._value, 1)}€"  # 0.0 -> 0
        )
