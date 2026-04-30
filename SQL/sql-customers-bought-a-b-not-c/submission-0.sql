-- Write your query below
SELECT customers.customer_id, customers.customer_name
FROM customers
WHERE customers.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'A'
)
AND customers.customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'B'
)
AND customers.customer_id NOT IN (
    SELECT customer_id FROM orders WHERE product_name = 'C'
)
ORDER BY customers.customer_name;