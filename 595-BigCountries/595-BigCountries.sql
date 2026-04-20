-- Last updated: 4/19/2026, 11:23:06 PM
# Write your MySQL query statement below

SELECT name, population, area
FROM World
WHERE (area >= 3000000) OR (population >= 25000000);