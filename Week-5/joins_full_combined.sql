-- ============================================================
-- Topic: SQL JOINs — INNER, LEFT, RIGHT, FULL
-- ============================================================

-- ============================================================
-- SETUP: schema + seed data
-- ============================================================

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id      INTEGER PRIMARY KEY,
    name    VARCHAR(50) NOT NULL,
    budget  DECIMAL(12, 2)
);

INSERT INTO departments (id, name, budget) VALUES
(1, 'Engineering', 500000.00),
(2, 'Marketing',   150000.00),
(3, 'Sales',       200000.00),
(4, 'HR',           90000.00),
(5, 'Legal',       120000.00);   -- no employees assigned yet

CREATE TABLE employees (
    id             INTEGER PRIMARY KEY,
    first_name     VARCHAR(50)  NOT NULL,
    last_name      VARCHAR(50)  NOT NULL,
    salary         DECIMAL(10, 2),
    hire_date      DATE,
    department_id  INTEGER REFERENCES departments(id)
);

INSERT INTO employees (id, first_name, last_name, salary, hire_date, department_id) VALUES
(1,  'Ananya', 'Rao',      85000.00, '2021-03-15', 1),
(2,  'Ravi',   'Kumar',    92000.00, '2019-07-01', 1),
(3,  'Sara',   'Fischer',  61000.00, '2022-01-10', 2),
(4,  'Wei',    'Chen',     78000.00, '2023-05-20', 1),
(5,  'Priya',  'Nair',     55000.00, '2020-11-02', 3),
(6,  'Lukas',  'Becker',   58000.00, '2021-09-14', 3),
(7,  'Meera',  'Iyer',     49000.00, '2018-04-23', 4),
(8,  'Tom',    'Schmidt',  64000.00, '2022-08-30', 2),
(9,  'Fatima', 'Ahmed',    99000.00, '2017-02-11', 1),
(10, 'Karan',  'Mehta',    53000.00, '2023-01-05', NULL);  -- not yet assigned to a department


-- ============================================================
-- PART 1: INNER JOIN
-- ============================================================
-- Returns only rows where there is a match in BOTH tables.
-- Karan (no department_id) and Legal (no employees) are excluded.

SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.id;

-- INNER JOIN with additional filtering
SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name,
    e.salary
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.id
WHERE e.salary > 60000
ORDER BY e.salary DESC;


-- ============================================================
-- PART 2: LEFT JOIN (LEFT OUTER JOIN)
-- ============================================================
-- Returns ALL rows from the left table (employees), plus matching
-- rows from the right table. Unmatched right-side columns are NULL.
-- Karan appears here with department_name = NULL.

SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.id;

-- Common use: find rows with NO match on the right side
-- (employees not assigned to any department)
SELECT
    e.first_name,
    e.last_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.id
WHERE d.id IS NULL;


-- ============================================================
-- PART 3: RIGHT JOIN (RIGHT OUTER JOIN)
-- ============================================================
-- Returns ALL rows from the right table (departments), plus matching
-- rows from the left table. Unmatched left-side columns are NULL.
-- Legal appears here with employee columns = NULL.

SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.id;

-- Common use: find departments with NO employees
SELECT
    d.name AS department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.id
WHERE e.id IS NULL;

-- Note: any RIGHT JOIN can be rewritten as a LEFT JOIN by swapping
-- table order — most people standardize on LEFT JOIN for consistency:
SELECT
    d.name AS department_name
FROM departments d
LEFT JOIN employees e
    ON e.department_id = d.id
WHERE e.id IS NULL;


-- ============================================================
-- PART 4: FULL JOIN (FULL OUTER JOIN)
-- ============================================================
-- Returns ALL rows from BOTH tables. Matches where possible,
-- NULL on whichever side has no match.
-- Karan (department_name NULL) and Legal (employee columns NULL)
-- both appear.

SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name
FROM employees e
FULL JOIN departments d
    ON e.department_id = d.id;

-- Find all unmatched rows from either side
SELECT
    e.first_name,
    e.last_name,
    d.name AS department_name
FROM employees e
FULL JOIN departments d
    ON e.department_id = d.id
WHERE e.id IS NULL OR d.id IS NULL;

-- MySQL doesn't support FULL JOIN — emulate it with UNION:
-- SELECT e.first_name, e.last_name, d.name AS department_name
-- FROM employees e LEFT JOIN departments d ON e.department_id = d.id
-- UNION
-- SELECT e.first_name, e.last_name, d.name AS department_name
-- FROM employees e RIGHT JOIN departments d ON e.department_id = d.id;


-- ============================================================
-- PART 5: JOIN combined with GROUP BY / aggregates
-- ============================================================

-- Headcount and total salary per department, including
-- departments with zero employees
SELECT
    d.name AS department_name,
    COUNT(e.id)       AS headcount,
    COALESCE(SUM(e.salary), 0) AS total_salary
FROM departments d
LEFT JOIN employees e
    ON e.department_id = d.id
GROUP BY d.name
ORDER BY total_salary DESC;