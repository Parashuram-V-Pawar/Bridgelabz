/* SUBQUERIES implementation */

-- Employees earning more than average salary.
SELECT e.employee_id,e.first_name, e.last_name, s.salary
FROM EMPLOYEES as e
JOIN SALARIES as s
ON e.employee_id = s.employee_id
WHERE s.salary > (SELECT AVG(s.salary)
				FROM SALARIES as s)

-- Employees with salary higher than their department average.
SELECT e.employee_id,e.first_name, e.last_name,d.dept_name, s.salary
FROM EMPLOYEES as e
JOIN DEPARTMENT as d
ON e.department_id = d.dept_no
JOIN SALARIES as s
ON e.employee_id = s.employee_id
WHERE s.salary > (SELECT AVG(s1.salary)
				FROM SALARIES as s1
				JOIN EMPLOYEES as e1
				ON e1.employee_id = s1.employee_id
				WHERE e1.department_id = e.department_id)

-- Employees in the department with highest employee count.
SELECT CONCAT(e.first_name,' ',e.last_name) as Emp_Name, d.dept_name
FROM EMPLOYEES as e
JOIN DEPARTMENT as d
ON e.department_id = d.dept_no
WHERE e.department_id = (SELECT TOP 1 department_id
					FROM EMPLOYEES
					GROUP BY department_id
					ORDER BY COUNT(*) DESC)

-- Employees with maximum salary.
SELECT CONCAT(e.first_name,' ',e.last_name) as Emp_Name, s.salary
FROM EMPLOYEES as e
JOIN SALARIES as s
ON e.employee_id = s.employee_id
WHERE s.salary = (SELECT TOP 1 salary
					FROM SALARIES
					ORDER BY salary DESC)

-- Employees whose salary is above average bonus amount.
SELECT CONCAT(e.first_name,' ',e.last_name) as Emp_Name, s.salary
FROM EMPLOYEES as e
JOIN SALARIES as s
ON e.employee_id = s.employee_id
WHERE s.salary > (SELECT AVG(bonus) as average_bonus
					FROM SALARIES)