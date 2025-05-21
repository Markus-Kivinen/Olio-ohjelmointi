SELECT fruit, MAX(value) as amount FROM Fruits GROUP BY fruit HAVING value > 5000;
