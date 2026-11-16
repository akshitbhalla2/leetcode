-- Last updated: 11/15/2026, 5:21:10 PM
# Write your MySQL query statement below


SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC