-- Last updated: 4/19/2026, 11:23:32 PM
# Write your MySQL query statement below


SELECT 
    P.firstName,
    P.lastName,
    A.city, 
    A.state
FROM Person AS P
LEFT JOIN Address AS A
ON P.personID=A.personID