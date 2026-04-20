-- Last updated: 4/19/2026, 11:23:04 PM
# Write your MySQL query statement below

UPDATE Salary
SET 
    sex = CASE 
        WHEN sex = "m" 
        THEN "f"
        ELSE "m"
    END 