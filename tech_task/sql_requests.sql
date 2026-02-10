-- Получение информации о сумме товаров заказанных под каждого клиента (Наименование клиента, сумма)
SELECT 
    customer.name,
    SUM(product.price * product_order.quantity) AS "sum"
FROM customer
LEFT JOIN customer_order ON customer.id = customer_order.customer_id 
LEFT JOIN product_order ON customer_order.id = product_order.order_id
left join product on product_order.product_id = product.id
GROUP BY customer.id;


-- Найти количество дочерних элементов первого уровня вложенности для категорий номенклатуры
SELECT 
    parent.name AS parent_category,
    COUNT(child.id) AS child_count
FROM category as parent
LEFT JOIN category as child ON parent.id = child.parent_id
GROUP BY parent.id;


--Написать текст запроса для отчета (view) «Топ-5 самых покупаемых товаров за последний месяц»
--(по количеству штук в заказах). В отчете должны быть: Наименование товара, Категория 1-го уровня,
--Общее количество проданных штук
WITH RECURSIVE recursive_table AS (
    SELECT id, name, id AS root_id, name AS root_name
    FROM category 
    WHERE parent_id IS NULL
    UNION
    SELECT category.id, category.name, recursive_table.root_id, recursive_table.root_name
    FROM category
    INNER JOIN recursive_table ON category.parent_id = recursive_table.id
)
SELECT
    product.name AS product_name,
    recursive_table.root_name AS root_category,
    SUM(product_order.quantity) AS sum_quantity
FROM product
INNER JOIN recursive_table ON product.category_id = recursive_table.id
INNER JOIN product_order ON product.id = product_order.product_id
INNER JOIN customer_order ON product_order.order_id = customer_order.id
    AND customer_order.order_date >= CURRENT_DATE - INTERVAL '1 MONTH'
    AND customer_order.order_date <= CURRENT_DATE
GROUP BY product.id, product.name, recursive_table.root_id, recursive_table.root_name
ORDER BY sum_quantity DESC
LIMIT 5;
