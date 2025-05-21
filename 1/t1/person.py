from dataclasses import dataclass


@dataclass
class Person:
    fname: str
    lname: str

    def fullname(self) -> None:
        print(f"{self.fname} {self.lname}")
        return None
