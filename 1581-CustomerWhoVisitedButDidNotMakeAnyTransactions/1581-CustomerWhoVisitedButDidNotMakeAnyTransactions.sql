-- Last updated: 11/15/2026, 5:21:19 PM
# Write your MySQL query statement below

SELECT A.customer_id, COUNT(A.customer_id) AS count_no_trans 
FROM (
    SELECT V.customer_id
    FROM Visits AS V
    LEFT JOIN Transactions AS T
    ON V.visit_id=T.visit_id
    WHERE T.transaction_id IS NULL
) AS A
GROUP BY A.customer_id;