--.mode table
SELECT receipt.cashier, receipt.created_at as receipt_date, product.name as product_name, product.price_per_kilo, product_receipt.amount FROM product
JOIN product_receipt
ON product.id = product_receipt.product_id
JOIN receipt
ON receipt.id = product_receipt.receipt_id
WHERE receipt.cashier = 'Vincent'
ORDER BY receipt.created_at DESC;
