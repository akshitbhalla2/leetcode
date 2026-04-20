-- Last updated: 4/19/2026, 11:22:10 PM
# Write your MySQL query statement below

SELECT 
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp)=2020 
GROUP BY user_id