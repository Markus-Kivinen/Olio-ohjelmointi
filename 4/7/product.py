import sqlite3
from dataclasses import dataclass
from typing import ClassVar

from db_conn import DB_CONN


@dataclass
class Product:
    manufacturer: str
    brand: str
    cost: float
    price: float

    conn: ClassVar[sqlite3.Connection] = DB_CONN
    cursor: ClassVar[sqlite3.Cursor] = conn.cursor()

    @staticmethod
    def createProduct() -> "Product":
        manufacturer = input("- Insert manufacturer: ")
        brand = input("- Insert brand: ")
        cost = float(input("- Insert cost: "))
        price = float(input("- Insert price: "))
        return Product(manufacturer, brand, cost, price)

    def insertDB(self) -> None:
        statement: str = (
            "INSERT INTO product (manufacturer, brand, cost, price) "
            "VALUES (?, ?, ?, ?);"
        )
        _ = Product.cursor.execute(
            statement,
            (self.manufacturer, self.brand, self.cost, self.price)
        )
        Product.conn.commit()
        return None

    @staticmethod
    def queryProducts(products: list["Product"]) -> list["Product"]:
        statement: str = "SELECT * FROM product;"
        prods: list[tuple[int, str, str, float, float]] = (
            Product.cursor.execute(statement).fetchall()
        )
        products = [
            Product(prod[1], prod[2], prod[3], prod[4])
            for prod in prods]
        return products
