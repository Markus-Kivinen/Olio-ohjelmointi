


--.mode table
WITH RECURSIVE FilteredFruit AS (
    --base
    SELECT name, vitamin, value
    FROM Fruit
    WHERE name NOT in  (
        SELECT name
        FROM Fruit
        WHERE vitamin = 'Folate (folic acid)'
    )
    --recursive
    UNION
    SELECT f.name, f.vitamin, f.value
    FROM Fruit f
    JOIN FilteredFruit ff ON f.name = ff.name
    WHERE f.vitamin != 'Folate (folic acid)'
)
SELECT name, vitamin, value 
FROM FilteredFruit
ORDER BY name DESC, vitamin;
