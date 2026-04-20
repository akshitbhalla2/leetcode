-- Last updated: 4/19/2026, 11:23:04 PM
# Write your MySQL query statement below

# SELECT 
#     T1.id,
#     CASE 
#         WHEN T1.p_id IS NULL THEN 'Root'
#         WHEN T2.dummy IS NULL THEN 'Leaf'
#         ELSE 'Inner'
#     END AS type
# FROM Tree AS T1
# LEFT JOIN (
#     SELECT DISTINCT p_id AS id, '1' AS dummy 
#     FROM Tree
# ) AS T2
# ON T1.id=T2.id


SELECT 
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN Id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
ORDER BY id





