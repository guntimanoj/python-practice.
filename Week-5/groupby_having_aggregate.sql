-- ============================================================
-- Topic: Aggregate functions, GROUP BY, HAVING
-- ============================================================

-- ============================================================
-- PART 1: Aggregate functions (no grouping)
-- ============================================================

-- COUNT — number of rows
SELECT COUNT(*) AS total_employees FROM employees;

-- COUNT a specific column — ignores NULLs
SELECT COUNT(email) AS employees_with_email FROM employees;

-- SUM
SELECT SUM(salary) AS total_payroll FROM employees;

-- AVG
SELECT AVG(salary) AS average_salary FROM employees;

-- MIN / MAX
SELECT MIN(salary) AS lowest_salary, MAX(salary) AS highest_salary
FROM employees;

-- Combine several in one query
SELECT
    COUNT(*)      AS headcount,
    SUM(salary)   AS total_payroll,
    AVG(salary)   AS avg_salary,
    MIN(salary)   AS min_salary,
    MAX(salary)   AS max_salary
FROM employees;


-- ============================================================
-- PART 2: GROUP BY — aggregate per category
-- ============================================================

-- Headcount per department
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department;

-- Average salary per department
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Multiple aggregates per group
SELECT
    department,
    COUNT(*)    AS headcount,
    SUM(salary) AS total_payroll,
    AVG(salary) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;

-- GROUP BY on multiple columns (department + hire year)
SELECT
    department,
    EXTRACT(YEAR FROM hire_date) AS hire_year,
    COUNT(*) AS headcount
FROM employees
GROUP BY department, hire_year
ORDER BY department, hire_year;


-- ============================================================
-- PART 3: WHERE vs HAVING
-- ============================================================
-- WHERE filters rows BEFORE grouping.
-- HAVING filters groups AFTER aggregation.
-- Aggregate functions cannot be used inside WHERE.

-- Departments with more than 3 employees
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
HAVING COUNT(*) > 3;

-- Departments with average salary above 65000
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 65000;

-- Combining WHERE (row-level filter) with HAVING (group-level filter)
SELECT department, AVG(salary) AS avg_salary
FROM employees
WHERE hire_date > '2019-01-01'
GROUP BY department
HAVING AVG(salary) > 60000
ORDER BY avg_salary DESC;


-- ============================================================
-- PART 4: Full pipeline — WHERE + GROUP BY + HAVING + ORDER BY + LIMIT
-- ============================================================

SELECT
    department,
    COUNT(*)    AS headcount,
    AVG(salary) AS avg_salary
FROM employees
WHERE salary >= 50000
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY avg_salary DESC
LIMIT 2;