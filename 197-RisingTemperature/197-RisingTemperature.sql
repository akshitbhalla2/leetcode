-- Last updated: 4/19/2026, 11:23:27 PM
# Write your MySQL query statement below

SELECT A.id
FROM Weather AS A
LEFT JOIN (
    SELECT 
        DATE_ADD(recordDate, INTERVAL 1 DAY) AS recordDate, 
        temperature AS temperature_prev
    FROM Weather
) AS B
ON A.recordDate=B.recordDate
WHERE A.temperature > B.temperature_prev;