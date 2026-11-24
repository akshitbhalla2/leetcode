-- Last updated: 4/19/2026, 11:22:25 PM
# Write your MySQL query statement below

# SELECT 
#     U.user_id AS buyer_id,
#     MAX(U.join_date) AS join_date,
#     SUM(
#         CASE WHEN YEAR(O.order_date)=2019 THEN 1 ELSE 0 END 
#     ) AS orders_in_2019
# FROM Users AS U
# LEFT JOIN Orders AS O
# ON U.user_id=O.buyer_id
# GROUP BY O.buyer_id

# UNION ALL

# SELECT 
#     O.buyer_id,
#     MAX(U.join_date) AS join_date,
#     0 AS orders_in_2019
# FROM Users AS U
# RIGHT JOIN Orders AS O
# ON U.user_id=O.buyer_id
# WHERE U.user_id IS NULL
# GROUP BY O.buyer_id

SELECT 
    U.user_id AS buyer_id,
    U.join_date,
    SUM(
        CASE WHEN YEAR(O.order_date)=2019 THEN 1 ELSE 0 END 
    ) AS orders_in_2019
FROM Users AS U
LEFT JOIN Orders AS O
ON U.user_id=O.buyer_id
GROUP BY 
    U.user_id,
    U.join_date

