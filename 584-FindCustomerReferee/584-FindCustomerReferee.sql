-- Last updated: 4/19/2026, 11:23:07 PM
# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE (referee_id != 2) OR (referee_id IS NULL);