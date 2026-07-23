============================================================
PostgreSQL Complete Program
Topics:
1. CREATE TABLE
2. INSERT
3. VIEW
4. STORED PROCEDURE
5. TRIGGER
===========================================================
------------------------------------------------------------
-- 1. CREATE TABLE
------------------------------------------------------------

DROP TABLE IF EXISTS employee_log;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees(
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary NUMERIC(10,2),
    joining_date DATE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------
-- 2. INSERT SAMPLE DATA
------------------------------------------------------------

INSERT INTO employees(name,department,salary,joining_date)
VALUES
('Manoj','IT',50000,'2025-01-15'),
('Rahul','HR',42000,'2024-08-20'),
('Priya','Finance',65000,'2023-03-10'),
('Anjali','IT',70000,'2022-06-18');

------------------------------------------------------------
-- 3. DISPLAY TABLE
------------------------------------------------------------

SELECT * FROM employees;

------------------------------------------------------------
-- 4. SIMPLE VIEW
------------------------------------------------------------

CREATE OR REPLACE VIEW employee_view AS
SELECT
    emp_id,
    name,
    department,
    salary
FROM employees;

SELECT * FROM employee_view;

------------------------------------------------------------
-- 5. JOIN VIEW
------------------------------------------------------------

DROP TABLE IF EXISTS departments;

CREATE TABLE departments(
    dept_name VARCHAR(30) PRIMARY KEY,
    manager VARCHAR(50)
);

INSERT INTO departments VALUES
('IT','David'),
('HR','John'),
('Finance','Maria');

CREATE OR REPLACE VIEW employee_department_view AS
SELECT
    e.name,
    e.department,
    d.manager,
    e.salary
FROM employees e
JOIN departments d
ON e.department=d.dept_name;

SELECT * FROM employee_department_view;

------------------------------------------------------------
-- 6. AGGREGATE VIEW
------------------------------------------------------------

CREATE OR REPLACE VIEW department_salary AS
SELECT
    department,
    COUNT(*) AS total_employees,
    AVG(salary) AS average_salary,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department;

SELECT * FROM department_salary;

------------------------------------------------------------
-- 7. STORED PROCEDURE - INSERT
------------------------------------------------------------

CREATE OR REPLACE PROCEDURE add_employee(
    p_name VARCHAR,
    p_department VARCHAR,
    p_salary NUMERIC,
    p_joining_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO employees(name,department,salary,joining_date)
    VALUES
    (
        p_name,
        p_department,
        p_salary,
        p_joining_date
    );
END;
$$;

CALL add_employee(
'Kiran',
'IT',
55000,
'2025-07-01'
);

SELECT * FROM employees;

------------------------------------------------------------
-- 8. STORED PROCEDURE - UPDATE
------------------------------------------------------------

CREATE OR REPLACE PROCEDURE update_salary(
    p_emp_id INT,
    p_new_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees
    SET salary=p_new_salary
    WHERE emp_id=p_emp_id;
END;
$$;

CALL update_salary(1,60000);

SELECT * FROM employees;

------------------------------------------------------------
-- 9. STORED PROCEDURE - DELETE
------------------------------------------------------------

CREATE OR REPLACE PROCEDURE delete_employee(
    p_emp_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM employees
    WHERE emp_id=p_emp_id;
END;
$$;

CALL delete_employee(2);

SELECT * FROM employees;

------------------------------------------------------------
-- 10. LOG TABLE
------------------------------------------------------------

CREATE TABLE employee_log(
    log_id SERIAL PRIMARY KEY,
    action TEXT,
    employee_name VARCHAR(50),
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

------------------------------------------------------------
-- 11. BEFORE INSERT TRIGGER
------------------------------------------------------------

CREATE OR REPLACE FUNCTION prevent_negative_salary()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.salary < 0 THEN
        RAISE EXCEPTION 'Salary cannot be negative';
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER before_insert_salary
BEFORE INSERT
ON employees
FOR EACH ROW
EXECUTE FUNCTION prevent_negative_salary();

------------------------------------------------------------
-- 12. AFTER INSERT TRIGGER
------------------------------------------------------------

CREATE OR REPLACE FUNCTION log_employee_insert()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO employee_log(action,employee_name)
    VALUES
    (
        'INSERT',
        NEW.name
    );

    RETURN NEW;
END;
$$;

CREATE TRIGGER after_insert_employee
AFTER INSERT
ON employees
FOR EACH ROW
EXECUTE FUNCTION log_employee_insert();

------------------------------------------------------------
-- TEST INSERT
------------------------------------------------------------

INSERT INTO employees
(name,department,salary,joining_date)
VALUES
(
'Ramesh',
'Finance',
45000,
'2025-02-10'
);

------------------------------------------------------------
-- 13. BEFORE UPDATE TRIGGER
------------------------------------------------------------

CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    NEW.last_updated=CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;

CREATE TRIGGER before_update_employee
BEFORE UPDATE
ON employees
FOR EACH ROW
EXECUTE FUNCTION update_timestamp();

------------------------------------------------------------
-- TEST UPDATE
------------------------------------------------------------

UPDATE employees
SET salary=80000
WHERE emp_id=1;

------------------------------------------------------------
-- 14. AFTER DELETE TRIGGER
------------------------------------------------------------

CREATE OR REPLACE FUNCTION log_employee_delete()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO employee_log(action,employee_name)
    VALUES
    (
        'DELETE',
        OLD.name
    );

    RETURN OLD;
END;
$$;

CREATE TRIGGER after_delete_employee
AFTER DELETE
ON employees
FOR EACH ROW
EXECUTE FUNCTION log_employee_delete();

------------------------------------------------------------
-- TEST DELETE
------------------------------------------------------------

DELETE FROM employees
WHERE emp_id=3;

------------------------------------------------------------
-- FINAL OUTPUT
------------------------------------------------------------

SELECT * FROM employees;

SELECT * FROM employee_view;

SELECT * FROM employee_department_view;

SELECT * FROM department_salary;

SELECT * FROM employee_log;