-- ============================================================
-- Topics: SELECT + WHERE
-- Run sample_data.sql first to create/populate the employees table.
-- ============================================================

-- ============================================================
-- PART 1: SELECT
-- ============================================================

-- 1. Select every column, every row
SELECT * FROM employees;

-- 2. Select specific columns only
SELECT first_name, last_name, department
FROM employees;

-- 3. Column aliasing with AS
SELECT
    first_name AS "First Name",
    last_name  AS "Last Name",
    salary     AS "Annual Salary"
FROM employees;

-- 4. DISTINCT — unique department names only
SELECT DISTINCT department
FROM employees;

-- 5. Expressions inside SELECT
SELECT
    first_name,
    last_name,
    salary,
    salary / 12 AS monthly_salary
FROM employees;

-- 6. Concatenating columns (SQLite/Postgres use ||, MySQL uses CONCAT())
SELECT
    first_name || ' ' || last_name AS full_name   -- SQLite / Postgres
    -- CONCAT(first_name, ' ', last_name) AS full_name  -- MySQL equivalent
FROM employees;


-- ============================================================
-- PART 2: WHERE
-- ============================================================

-- 1. Basic comparison operators
SELECT * FROM employees WHERE department = 'Engineering';
SELECT * FROM employees WHERE salary > 70000;
SELECT * FROM employees WHERE salary >= 60000;
SELECT * FROM employees WHERE department != 'Sales';

-- 2. AND / OR / NOT
SELECT * FROM employees
WHERE department = 'Engineering' AND salary > 85000;

SELECT * FROM employees
WHERE department = 'Sales' OR department = 'HR';

SELECT * FROM employees
WHERE NOT department = 'Marketing';

-- 3. Operator precedence — parentheses matter!
SELECT * FROM employees
WHERE department = 'Sales' OR department = 'HR' AND salary > 50000;
-- vs. the (usually intended) version:
SELECT * FROM employees
WHERE (department = 'Sales' OR department = 'HR') AND salary > 50000;

-- 4. BETWEEN — inclusive range
SELECT * FROM employees
WHERE salary BETWEEN 55000 AND 90000;

-- 5. IN — match against a list
SELECT * FROM employees
WHERE department IN ('Engineering', 'Marketing');

-- 6. LIKE — pattern matching
SELECT * FROM employees WHERE first_name LIKE 'A%';      -- starts with A
SELECT * FROM employees WHERE last_name LIKE '%a';        -- ends with a
SELECT * FROM employees WHERE first_name LIKE '_a%';      -- 2nd letter is a

-- 7. IS NULL / IS NOT NULL
SELECT * FROM employees WHERE email IS NULL;
SELECT * FROM employees WHERE email IS NOT NULL;
-- Note: WHERE email = NULL never works — NULL isn't comparable with =

-- ============================================================
-- PART 3: SELECT + WHERE together
-- ============================================================

SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering' AND salary > 80000;