-- Last updated: 4/19/2026, 11:22:26 PM
# Write your MySQL query statement below


SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity AS A
WHERE 
    (activity_date <= '2019-07-27') 
    AND (activity_date >  DATE_SUB('2019-07-27', INTERVAL 30 DAY)) 
GROUP BY 
    activity_date
HAVING COUNT(DISTINCT user_id) > 0
ORDER BY 
    activity_date