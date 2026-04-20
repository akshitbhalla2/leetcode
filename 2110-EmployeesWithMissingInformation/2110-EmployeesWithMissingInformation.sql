-- Last updated: 4/19/2026, 11:22:08 PM
# Write your MySQL query statement below

SELECT * FROM (
    SELECT E.employee_id
    FROM Employees AS E
    LEFT JOIN Salaries AS S
    ON E.employee_id=S.employee_id
    WHERE S.salary IS NULL
    UNION ALL
    SELECT S.employee_id
    FROM Employees AS E
    RIGHT JOIN Salaries AS S
    ON E.employee_id=S.employee_id
    WHERE E.name IS NULL
) AS A
ORDER BY A.employee_id