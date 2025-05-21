import sqlite3

from db_conn import DB_CONN


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.conn: sqlite3.Connection = DB_CONN
        print("Program ending.")
        self.conn.commit()
        self.conn.close()
        return None


if __name__ == "__main__":
    database = Main()
