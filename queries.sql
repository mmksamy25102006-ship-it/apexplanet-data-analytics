SELECT * FROM superstore;

SELECT Category,
SUM(Sales)
FROM superstore
GROUP BY Category;

SELECT *
FROM superstore
WHERE Sales>500;

SELECT *
FROM superstore
ORDER BY Sales DESC
LIMIT 10;