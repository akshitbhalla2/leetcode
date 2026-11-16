-- Last updated: 11/15/2026, 5:21:16 PM
# Write your MySQL query statement below


SELECT 
    U.name,
    T.balance
FROM Users AS U
LEFT JOIN (
    SELECT 
        account,
        SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
) AS T
ON U.account=T.account
WHERE T.balance > 10000