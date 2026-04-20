-- Last updated: 4/19/2026, 11:23:05 PM
# Write your MySQL query statement below

# SELECT sp.name
# FROM SalesPerson AS sp
# LEFT JOIN Orders AS o
# ON sp.sales_id=o.sales_id
# LEFT JOIN Company AS c
# ON o.com_id=c.com_id
# GROUP BY sp.name
# HAVING SUM(
#     CASE 
#         WHEN c.name='RED' THEN 1 
#         ELSE 0 
#     END
# ) = 0


SELECT s.name
FROM salesperson s
WHERE s.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders AS o
    LEFT JOIN company AS c 
    ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)