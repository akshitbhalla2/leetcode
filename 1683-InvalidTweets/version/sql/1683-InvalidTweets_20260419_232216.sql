-- Last updated: 4/19/2026, 11:22:16 PM
# Write your MySQL query statement below


SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;