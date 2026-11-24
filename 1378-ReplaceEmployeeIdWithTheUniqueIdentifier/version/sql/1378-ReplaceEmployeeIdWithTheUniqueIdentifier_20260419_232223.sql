-- Last updated: 4/19/2026, 11:22:23 PM
# Write your MySQL query statement below

SELECT B.unique_id, A.name
FROM Employees AS A
LEFT JOIN EmployeeUNI AS B
ON A.id=B.id;