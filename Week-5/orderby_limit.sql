-- ============================================================
-- Topics: ORDER BY + LIMIT
-- Run sample_data.sql first to create/populate the employees table.
-- ============================================================

-- ============================================================
-- PART 1: ORDER BY
-- ============================================================

-- 1. Default sort is ascending (ASC)
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary;

-- 2. Explicit ASC / DESC
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;

-- 3. Sort by multiple columns
SELECT first_name, last_name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;

-- 4. Sort by column position (works, but avoid in production code)
SELECT first_name, last_name, salary
FROM employees
ORDER BY 3 DESC;

-- 5. ORDER BY combined with WHERE
SELECT first_name, last_name, department, salary
FROM employees
WHERE department = 'Engineering'
ORDER BY salary DESC;

-- 6. Sorting on an expression, not just a raw column
SELECT first_name, last_name, salary, salary / 12 AS monthly_salary
FROM employees
ORDER BY monthly_salary DESC;


-- ============================================================
-- PART 2: LIMIT / OFFSET
-- ============================================================

-- 1. Basic LIMIT — first 5 rows (order is undefined without ORDER BY!)
SELECT * FROM employees LIMIT 5;

-- 2. Always pair LIMIT with ORDER BY for predictable results
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC
LIMIT 5;                              -- top 5 highest earners

-- 3. LIMIT + OFFSET for pagination
-- Page 1 (rows 1-5)
SELECT first_name, last_name, salary
FROM employees
ORDER BY id
LIMIT 5 OFFSET 0;

-- Page 2 (rows 6-10)
SELECT first_name, last_name, salary
FROM employees
ORDER BY id
LIMIT 5 OFFSET 5;

-- 4. Classic "top N per criteria" pattern
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary ASC
LIMIT 3;                              -- 3 lowest-paid employees

-- 5. Combining WHERE + ORDER BY + LIMIT
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'Engineering'
ORDER BY salary DESC
LIMIT 1;                              -- highest-paid engineer

-- ============================================================
-- PART 3: ORDER BY + LIMIT together (full pipeline)
-- ============================================================

SELECT first_name, last_name, department, salary
FROM employees
WHERE department IN ('Engineering', 'Sales')
ORDER BY salary DESC
LIMIT 5;