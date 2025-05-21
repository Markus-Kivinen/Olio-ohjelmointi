SELECT 
    group_id as [group], SUM(ects) as [total ects] 
FROM 
    Students group by group_id;
