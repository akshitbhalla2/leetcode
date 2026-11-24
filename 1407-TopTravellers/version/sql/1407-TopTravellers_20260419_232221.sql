-- Last updated: 4/19/2026, 11:22:21 PM
# Write your MySQL query statement below


SELECT U.name, COALESCE(SUM(R.distance), 0) AS travelled_distance
FROM Users as U 
LEFT JOIN Rides AS R
ON U.id=R.user_id
GROUP BY R.user_id
ORDER BY travelled_distance DESC, U.name ASC