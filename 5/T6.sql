--.mode table
SELECT Employee.FirstName, Employee.LastName
    FROM Employee
    WHERE Employee.ReportsTo = 
        (SELECT Employee.EmployeeId FROM Employee WHERE Employee.FirstName = 'Nancy' AND Employee.LastName = 'Edwards')
    ORDER BY Employee.FirstName ASC, Employee.LastName Asc