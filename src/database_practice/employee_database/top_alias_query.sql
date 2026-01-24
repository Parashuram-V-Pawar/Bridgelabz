/* Demonstration of TOP, ALIASES clauses */

-- Show top 5 highest paid employees.
SELECT TOP(5) *
FROM EMPLOYEES

-- Show top 10 recently hired employees.
SELECT TOP(10) *
FROM EMPLOYEES
ORDER BY hire_date DESC

-- Rename first_name as FirstName in output.
SELECT first_name as FirstName
FROM EMPLOYEES

-- Rename salary as AnnualSalary.
SELECT salary as AnnualSalary
FROM SALARIES

-- Show top 3 employees with highest bonus.
SELECT TOP(3) e.first_name, e.last_name, s.bonus
FROM SALARIES as s
JOIN EMPLOYEES as e
ON s.employee_id = e.employee_id
ORDER BY bonus DESC