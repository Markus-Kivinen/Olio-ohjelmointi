import sqlite3

from db_conn import DB_CONN
from menu_product import MenuProduct as Menu
from product import Product

PRODUCT_TABLE_STATEMENT: str = """CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    cost REAL NOT NULL,
    price REAL NOT NULL
);"""


class Main:
    def __init__(self) -> None:
        print("Program starting.")
        self.conn: sqlite3.Connection = DB_CONN
        self.cursor: sqlite3.Cursor = self.conn.cursor()
        self.running: bool = True
        self.menu: Menu = Menu()
        self.menu.add_option(1, "Add product", self.add_product)
        self.menu.add_option(2, "Show products", self.show_products)
        self.menu.add_option(0, "Exit", self.disconnect)
        self.create_table()
        self.run()
        return None

    def create_table(self) -> None:
        _ = self.cursor.execute(PRODUCT_TABLE_STATEMENT)

    def run(self) -> None:
        options = self.menu.options
        try:
            while self.running:
                self.menu.showOptions()
                choice = self.menu.askChoice()
                if not self.menu.has_option(choice):
                    print("Unknown option, try again.\n")
                    continue
                menu_func = options[choice].func
                if not menu_func:
                    print(f"'{options[choice].name}' not implemented yet.\n")
                else:
                    menu_func()
        except KeyboardInterrupt:
            self.disconnect()
        return None

    def add_product(self) -> None:
        print("Insert product details below:")
        prod = Product.createProduct()
        print("Adding product...")
        prod.insertDB()
        print("Product added!\n")

    def show_products(self) -> None:
        products: list[Product] = Product.queryProducts([])
        print("No., Manufacturer, Brand, Cost, Price")
        for i, p in enumerate(products, start=1):
            print(f"{i}, {p.manufacturer}, {p.brand}, {p.cost}, {p.price}")
        print("")
        return None

    def disconnect(self) -> None:
        print("Program ending.")
        self.conn.commit()
        self.conn.close()
        self.running = False
        return None


if __name__ == "__main__":
    database = Main()
