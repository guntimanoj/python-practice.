-- ==========================================================
-- PostgreSQL Complete Database Project
-- Topics Covered:
-- ✔ PRIMARY KEY
-- ✔ FOREIGN KEY
-- ✔ NOT NULL
-- ✔ UNIQUE
-- ✔ CHECK
-- ✔ DEFAULT
-- ✔ ON DELETE CASCADE
-- ✔ INDEX
-- ✔ COMPOSITE INDEX
-- ✔ EXPLAIN ANALYZE
-- ==========================================================

-- Remove old tables
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

------------------------------------------------------------
-- CUSTOMERS TABLE
------------------------------------------------------------

CREATE TABLE customers(
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK(age >= 18),
    city VARCHAR(50) DEFAULT 'Hyderabad'
);

------------------------------------------------------------
-- PRODUCTS TABLE
------------------------------------------------------------

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC CHECK(price > 0),
    stock INT CHECK(stock >= 0)
);

------------------------------------------------------------
-- ORDERS TABLE
------------------------------------------------------------

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT CHECK(quantity > 0),

    FOREIGN KEY(customer_id)
    REFERENCES customers(customer_id)
    ON DELETE CASCADE,

    FOREIGN KEY(product_id)
    REFERENCES products(product_id)
);

------------------------------------------------------------
-- INSERT CUSTOMERS
------------------------------------------------------------

INSERT INTO customers(customer_name,email,age,city)
VALUES
('Manoj','manoj@gmail.com',22,'Hyderabad'),
('Rahul','rahul@gmail.com',25,'Delhi'),
('Priya','priya@gmail.com',23,'Mumbai'),
('Sneha','sneha@gmail.com',24,DEFAULT);

------------------------------------------------------------
-- INSERT PRODUCTS
------------------------------------------------------------

INSERT INTO products(product_name,price,stock)
VALUES
('Laptop',70000,20),
('Phone',25000,40),
('Tablet',30000,15),
('Headphones',5000,60);

------------------------------------------------------------
-- INSERT ORDERS
------------------------------------------------------------

INSERT INTO orders(customer_id,product_id,quantity)
VALUES
(1,1,1),
(1,4,2),
(2,2,1),
(3,3,2),
(4,2,1);

------------------------------------------------------------
-- VIEW ALL TABLES
------------------------------------------------------------

SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;

------------------------------------------------------------
-- INNER JOIN
------------------------------------------------------------

SELECT
o.order_id,
c.customer_name,
p.product_name,
o.quantity,
p.price,
(o.quantity * p.price) AS total_amount
FROM orders o
JOIN customers c
ON o.customer_id = c.customer_id
JOIN products p
ON o.product_id = p.product_id;

------------------------------------------------------------
-- AGGREGATE FUNCTIONS
------------------------------------------------------------

SELECT
c.customer_name,
SUM(o.quantity * p.price) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN products p
ON o.product_id = p.product_id
GROUP BY c.customer_name;

------------------------------------------------------------
-- CHECK DEFAULT VALUE
------------------------------------------------------------

SELECT customer_name,city
FROM customers;

------------------------------------------------------------
-- UNIQUE CONSTRAINT TEST
------------------------------------------------------------

-- This will generate an error

-- INSERT INTO customers(customer_name,email,age)
-- VALUES ('Test','manoj@gmail.com',22);

------------------------------------------------------------
-- CHECK CONSTRAINT TEST
------------------------------------------------------------

-- This will generate an error

-- INSERT INTO products(product_name,price,stock)
-- VALUES ('TV',-1000,5);

------------------------------------------------------------
-- CREATE INDEX
------------------------------------------------------------

CREATE INDEX idx_customer_city
ON customers(city);

------------------------------------------------------------
-- COMPOSITE INDEX
------------------------------------------------------------

CREATE INDEX idx_product_price
ON products(product_name,price);

------------------------------------------------------------
-- EXPLAIN ANALYZE
------------------------------------------------------------

EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE city='Delhi';

------------------------------------------------------------
-- DELETE CASCADE DEMONSTRATION
------------------------------------------------------------

DELETE FROM customers
WHERE customer_id=2;

------------------------------------------------------------
-- Verify customer deleted
------------------------------------------------------------

SELECT * FROM customers;

------------------------------------------------------------
-- Verify related orders deleted automatically
------------------------------------------------------------

SELECT * FROM orders;

------------------------------------------------------------
-- INDEX SEARCH
------------------------------------------------------------

SELECT *
FROM customers
WHERE city='Hyderabad';

------------------------------------------------------------
-- FINAL REPORT
------------------------------------------------------------

SELECT
c.customer_name,
COUNT(o.order_id) AS total_orders,
COALESCE(SUM(o.quantity*p.price),0) AS total_purchase
FROM customers c
LEFT JOIN orders o
ON c.customer_id=o.customer_id
LEFT JOIN products p
ON o.product_id=p.product_id
GROUP BY c.customer_name
ORDER BY total_purchase DESC;