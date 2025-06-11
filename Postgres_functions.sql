SELECT * FROM cars
WHERE brand = 'Volvo';

SELECT * FROM cars
WHERE year::int > 1975;

SELECT * FROM cars
WHERE year::int < 1975;

SELECT * FROM cars
WHERE model LIKE 'M%' ---That starts with the letter M---

SELECT * FROM cars
WHERE model ILIKE 'm&'

SELECT * FROM cars
WHERE brand = 'Volvo' AND year::int = 1968;


SELECT * FROM cars
WHERE brand = 'Volvo' OR year::int = 1968;

---return all records where the brand us present in this list
SELECT * FROM cars
WHERE brand in ('Volvo', 'Mercedes', 'Ford')

---return all records where the brand is not present in this list
SELECT * FROM cars
WHERE brand NOT in ('Volvo', 'Mercedes', 'Ford')

--Between operator is used to check if a column's value is between a specified range of values
SELECT * FROM cars
WHERE year::int BETWEEN 1970 AND 1980

--The result returns all records that are alphabetically between the specified values.
SELECT * FROM products
WHERE product_name BETWEEN 'Pavlova' AND 'Tofu'
ORDER BY product_name

--Select all orders between 12th April to 5th May
SELECT * FROM orders
WHERE order_date BETWEEN '2023-04-12' AND '2023-05-05'

--NOT Between operator is used to check if a column's value is between a specified range of values
SELECT * FROM cars
WHERE year::int NOT BETWEEN 1970 AND 1980

--Return all record where the brand does not start with a capital B
SELECT * FROM cars
WHERE brand NOT LIKE 'B%'

---Case sensitive ilike
SELECT * FROM cars
WHERE brand NOT ILIKE 'B%'
SELECT * FROM cars
WHERE brand in ('Volvo', 'Mercedes', 'Ford')

--Select only the DISTINCT values from the country column in the customers table:
SELECT DISTINCT country FROM customers

--Return the number of different countries there are in the customers table
SELECT COUNT(DISTINCT country) FROM customers

SELECT * FROM customers
WHERE city = 'London'

--Sort the table by price
SELECT * FROM products
ORDER BY price DESC

--First 20
SELECT * FROM customers

--Return 20 records, starting from the 41th record:
SELECT * FROM customers
LIMIT 20 OFFSET 40

--Lowest price in the products table
SELECT MIN(price) AS Lowest_price
FROM products

--Highest price in the products table
SELECT MAX(price) AS Highest_price
FROM products

--Null values are not counted
SELECT COUNT (customer_id)
FROM customers

SELECT COUNT (customer_id)
FROM customers
WHERE city = 'London'

--Return the total ammount of ordered items
SELECT SUM(quantity) AS total_quantity
FROM order_details

--Return the average price of all the products in the products table
SELECT AVG (customer_id)::NUMERIC(10, 2) --Rounded to 2 dp
FROM customers

--Return all customers with a name that contains the letter A
SELECT * FROM customers
WHERE customer_name LIKE '&A&'

SELECT * FROM customers
WHERE customer_name ILIKE '&a&'

SELECT * FROM customers
WHERE customer_name LIKE '&en'

--Return all customers from a city that starts with 'L' followed by one wildcard character, then 'nd' and then two wildcard characters:
SELECT * FROM customers
WHERE city LIKE 'L_nd__'

--Return all customers that have an order in the orders table:
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders


--Return all customers that DO NOT have an order in the orders table:
SELECT * FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders)

---The IN operator can be used instead of several OR statements.

--Concatenate, with space
SELECT product_name || ' ' || UNIT AS products
FROM products

--JOINS selects records that have matching values in both tables:
--Joins products to categories using the category_id column

--Inner joins selects records that have matching values
--Joins products to categories using the category_id column

-- Corrected join with actual column name
SELECT product_id, product_name, category_name
FROM products 
INNER JOIN categories ON products.category_id = categories.categogy_id;

SELECT testproduct_id, product_name, category_name
FROM testproducts
INNER JOIN categories ON testproducts.category_id = categories.categogy_id;

--Left join selects all records from the left teble and the matching records from the right table
--Join testproducts to categories using the category_id column:
SELECT testproduct_id, product_name, category_name
FROM testproducts
LEFT JOIN categories ON testproducts.category_id = categories.categogy_id;

--Right join selects all records from the Right teble and the matching records from the left table
--Join testproducts to categories using the category_id column:
SELECT testproduct_id, product_name, category_name
FROM testproducts
RIGHT JOIN categories ON testproducts.category_id = categories.categogy_id;

--FULL JOIN we will get all records from both the categories table and the testproducts table:
SELECT testproduct_id, product_name, category_name
FROM testproducts
FULL JOIN categories ON testproducts.category_id = categories.categogy_id;

--CROSS JOIN matches all records from the left table with EACH record from the right table.
--All the records from the right table will be returned for each record in the left table
SELECT testproduct_id, product_name, category_name
FROM testproducts
CROSS JOIN categories;

--The union operator pnly returns the exact same result, only one row will be listed
SELECT product_id
FROM products
UNION
SELECT testproduct_id
FROM testproducts
ORDER BY product_id

--Lists the number of customers in each country:
SELECT COUNT(customer_id), country
FROM customers
GROUP BY country

--lists the number of orders made by each customer:
SELECT customers.customer_name, COUNT(orders.order_id)
from orders 
LEFT JOIN customers ON orders.customer_id = customers.customer_id
GROUP BY customer_name
