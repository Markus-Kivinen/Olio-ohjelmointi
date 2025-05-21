SELECT city, COUNT(owner) FROM Accounts GROUP BY city HAVING COUNT(owner) > 4;
