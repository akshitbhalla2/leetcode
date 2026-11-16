-- Last updated: 11/15/2026, 5:21:12 PM
# Write your MySQL query statement below


SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;