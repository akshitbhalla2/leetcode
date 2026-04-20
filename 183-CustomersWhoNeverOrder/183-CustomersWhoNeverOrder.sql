-- Last updated: 4/19/2026, 11:23:30 PM
# Write your MySQL query statement below


# SELECT C.name AS Customers
# FROM (
#     SELECT A.name, B.customerId
#     FROM Customers AS A
#     LEFT JOIN Orders AS B
#     ON A.ID = B.customerId
# ) AS C
# WHERE C.customerId IS NULL


SELECT A.name AS Customers
FROM Customers AS A
LEFT JOIN Orders AS B
ON A.ID = B.customerId
WHERE B.customerId IS NULL