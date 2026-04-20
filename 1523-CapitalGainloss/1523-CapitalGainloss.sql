-- Last updated: 4/19/2026, 11:22:22 PM
# Write your MySQL query statement below

# SELECT 
#     A.stock_name,
#     SUM(A.price) AS capital_gain_loss
# FROM (
#     SELECT 
#         stock_name,
#         CASE 
#             WHEN operation='Sell' THEN price
#             ELSE -price
#         END AS price
#     FROM Stocks
# ) AS A
# GROUP BY A.stock_name


select stock_name,sum(if(operation='Buy',-(price),(price))) 
as capital_gain_loss from Stocks group by stock_name 