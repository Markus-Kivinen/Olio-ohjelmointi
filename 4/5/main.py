import sqlite3
from types import TracebackType

from db_conn import DB_CONN

PRODUCT_TABLE_STATEMENT: str = """CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    cost REAL NOT NULL,
    price REAL NOT NULL
);
"""


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.conn: sqlite3.Connection = DB_CONN
        self.cursor: sqlite3.Cursor = self.conn.cursor()
        self.create_table()
        self.add_product()
        self.disconnect()
        return None

    def create_table(self) -> None:
        _ = self.cursor.execute(PRODUCT_TABLE_STATEMENT)

    def add_product(self) -> None:
        print("Insert product details below:")
        m = input("- Insert manufacturer: ")
        b = input("- Insert brand: ")
        c = input("- Insert cost: ")
        p = input("- Insert price: ")
        print("Storing product details into the database...")
        statement: str = (
            "INSERT INTO product (manufacturer, brand, cost, price) "
            "VALUES (?, ?, ?, ?);"
        )
        _ = self.cursor.execute(statement, (m, b, c, p))

    def disconnect(self) -> None:
        self.conn.commit()
        self.conn.close()
        print("Program ending.")
        return None

    def __enter__(self) -> "Main":
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        # self.disconnect() tarkistin  ei hyväksy
        return None


if __name__ == "__main__":
    with Main() as db:
        # self.create_table() tarkistin  ei hyväksy
        # self.add_product() tarkistin  ei hyväksy
        pass
