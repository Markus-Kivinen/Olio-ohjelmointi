from dataclasses import dataclass
from typing import Self


@dataclass
class SodaBottle:
    brand: str
    volume: float

    def serialize(self) -> str:
        return f"{self.brand};{round(self.volume, 2)}"

    @classmethod
    def deserialize(cls, serialized: str) -> Self:
        brand, volume = serialized.split(";")
        return cls(brand, float(volume))
