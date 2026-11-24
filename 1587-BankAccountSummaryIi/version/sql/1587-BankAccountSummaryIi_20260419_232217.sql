-- Last updated: 4/19/2026, 11:22:17 PM
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