.mode table
.headers ON
SELECT
    id as [opiskelija tunnus], name as nimi, group_id as ryhma, ects as ECTS
FROM
    Students S
WHERE
    S.ects = (SELECT MAX(ects) FROM Students WHERE group_id = S.group_id)
ORDER BY
    group_id;
