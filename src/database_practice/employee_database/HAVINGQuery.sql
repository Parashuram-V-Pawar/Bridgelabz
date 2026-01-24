/* HAVING Clause implementation */

-- Departments having more than 5 employees.
SELECT d.dept_name, COUNT(e.employee_id) as Employee_Count
FROM DEPARTMENT as d
INNER JOIN EMPLOYEES as e
ON d.dept_no = e.department_id
GROUP BY d.dept_name
HAVING COUNT(e.employee_id) > 5

-- Departments with average salary > 80,000.
SELECT d.dept_name, AVG(s.salary) as Average_Salary
FROM DEPARTMENT as d
INNER JOIN EMPLOYEES as e
ON d.dept_no = e.department_id
INNER JOIN SALARIES as s
ON e.employee_id = s.employee_id
GROUP BY d.dept_name
HAVING AVG(s.salary) > 80000

-- Job roles having more than 5 employees.
SELECT j.job_title, COUNT(e.employee_id) as Employee_Count
FROM JOB as j
INNER JOIN EMPLOYEES as e
ON j.job_id = e.job_id
GROUP BY j.job_title
HAVING COUNT(e.employee_id) > 5

-- Pay grades having average salary > 85,000.
SELECT s.pay_grade, AVG(s.salary) as Average_Salary
FROM SALARIES as s
INNER JOIN EMPLOYEES as e
ON e.employee_id = s.employee_id
GROUP BY s.pay_grade
HAVING AVG(s.salary) > 85000

-- Departments where total salary exceeds 400,000.
SELECT d.dept_name, SUM(s.salary) as Average_Salary
FROM DEPARTMENT as d
INNER JOIN EMPLOYEES as e
ON e.department_id = d.dept_no
INNER JOIN SALARIES as s
ON e.employee_id = s.employee_id
GROUP BY d.dept_name
HAVING SUM(s.salary) > 400000