-- Last updated: 11/15/2026, 5:21:37 PM
# Write your MySQL query statement below

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id=viewer_id
ORDER BY author_id ASC;