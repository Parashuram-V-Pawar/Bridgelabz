/* Demoonstration of DISTINCT, ORDER BY Clause */

-- Show distinct job IDs used by employees.
SELECT DISTINCT(job_id)
FROM EMPLOYEES

-- Order employees by hire_date (oldest first).
SELECT * 
FROM EMPLOYEES
ORDER BY hire_date ASC

-- Order salaries from highest to lowest.
SELECT *
FROM SALARIES
ORDER BY salary DESC

-- Display distinct pay grades.
SELECT DISTINCT(pay_grade)
FROM SALARIES

-- Order employees by last name alphabetically.
SELECT * 
FROM EMPLOYEES
ORDER BY last_name ASC