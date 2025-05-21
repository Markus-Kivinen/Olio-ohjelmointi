from dataclasses import dataclass


@dataclass
class SodaBottle:
    brand: str
    volume: float

    def serialize(self) -> str:
        return f"{self.brand};{round(self.volume, 2)}"
