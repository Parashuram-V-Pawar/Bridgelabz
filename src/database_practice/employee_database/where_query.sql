/* WHERE Query Demonstration*/
SELECT * FROM EMPLOYEES

-- Find all female employees.
SELECT employee_id,first_name,last_name FROM EMPLOYEES
WHERE gender = 'F';

-- Find employees hired after 2020-01-01.
SELECT employee_id, first_name, last_name
FROM EMPLOYEES
WHERE hire_date > '2020-01-01';

-- Show employees working in department 5.
SELECT employee_id, first_name, last_name
FROM EMPLOYEES
WHERE department_id = 5;

-- List employees with job_id = 7.
SELECT employee_id, first_name, last_name
FROM EMPLOYEES
WHERE job_id = 7;

-- Find salaries greater than 80,000.
SELECT employee_id, salary
FROM SALARIES
WHERE salary > 80000;

