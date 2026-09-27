-- Write your query below

BEGIN;
ALTER TABLE orders RENAME id TO order_id;

SELECT name
FROM customers c
LEFT JOIN orders o ON o.customer_id=c.id
WHERE o.order_id IS NULL;

COMMIT;