-- Last updated: 4/19/2026, 11:22:26 PM
# Write your MySQL query statement below

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id=viewer_id
ORDER BY author_id ASC;