/* Demonstration of GROUP BY Clause */

-- Count number of employees in each department.
SELECT d.dept_name, COUNT(e.first_name) as count_of_employees
FROM EMPLOYEES as e
INNER JOIN DEPARTMENT as d
ON e.department_id = d.dept_no
GROUP BY d.dept_name

-- Find average salary per department.
SELECT d.dept_name, avg(s.salary) as Average_Salary
From SALARIES as s
INNER JOIN EMPLOYEES as e
ON e.employee_id = s.employee_id
INNER JOIN DEPARTMENT as d
ON d.dept_no = e.department_id
GROUP BY d.dept_name

-- Find total bonus paid per department.
SELECT d.dept_name, SUM(s.bonus) as TOTAL_BONUS_PAID
FROM DEPARTMENT as d
INNER JOIN EMPLOYEES as e
ON e.department_id = d.dept_no
INNER JOIN SALARIES as s
ON e.employee_id = s.employee_id
GROUP BY d.dept_name

-- Count employees by gender.
SELECT gender, COUNT(employee_id) as Count_of_Employees
FROM EMPLOYEES
GROUP BY gender

-- Find highest salary in each department.
SELECT d.dept_name, MAX(s.salary) as Highest_Salaries
FROM DEPARTMENT as d
INNER JOIN EMPLOYEES as e
ON d.dept_no = e.department_id
INNER JOIN SALARIES as s
ON e.employee_id = s.employee_id
GROUP BY d.dept_name
