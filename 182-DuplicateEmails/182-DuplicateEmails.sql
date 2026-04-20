-- Last updated: 4/19/2026, 11:23:31 PM
# Write your MySQL query statement below

SELECT email 
FROM Person
GROUP BY email
HAVING COUNT(email) > 1