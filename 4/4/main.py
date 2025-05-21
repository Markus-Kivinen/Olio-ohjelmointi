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
        self.disconnect()
        return None

    def create_table(self) -> None:
        _ = self.cursor.execute(PRODUCT_TABLE_STATEMENT)

    def disconnect(self) -> None:
        print("Program ending.")
        self.conn.commit()
        self.conn.close()
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
        pass
