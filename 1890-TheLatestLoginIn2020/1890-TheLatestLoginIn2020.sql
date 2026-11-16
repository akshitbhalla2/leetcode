-- Last updated: 11/15/2026, 5:21:01 PM
# Write your MySQL query statement below

SELECT 
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp)=2020 
GROUP BY user_id