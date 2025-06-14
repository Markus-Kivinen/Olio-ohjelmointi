--.mode table
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS receipt;
DROP TABLE IF EXISTS product_receipt;

CREATE TABLE IF NOT EXISTS product(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  price_per_kilo NUMERIC NOT NULL
);

CREATE TABLE IF NOT EXISTS receipt(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cashier TEXT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_receipt(
  amount NUMERIC NOT NULL,
  product_id INTEGER NOT NULL,
  receipt_id INTEGER NOT NULL,
  FOREIGN KEY(product_id) REFERENCES product(id),
  FOREIGN KEY(receipt_id) REFERENCES receipt(id)
);

.mode csv
.import --skip 1 t4_product.csv product
.import --skip 1 t4_receipt.csv receipt
.import --skip 1 t4_product_receipt.csv product_receipt
