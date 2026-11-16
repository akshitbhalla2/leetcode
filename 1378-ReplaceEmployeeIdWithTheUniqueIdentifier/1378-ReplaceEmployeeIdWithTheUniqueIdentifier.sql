-- Last updated: 11/15/2026, 5:21:31 PM
# Write your MySQL query statement below

SELECT B.unique_id, A.name
FROM Employees AS A
LEFT JOIN EmployeeUNI AS B
ON A.id=B.id;