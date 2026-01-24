/* JOINS implementation */

-- Show employee name with department name.
SELECT e.first_name, e.last_name, d.dept_name
FROM EMPLOYEES as e
INNER JOIN DEPARTMENT as d
ON e.department_id = d.dept_no

-- Show employee name with job title.
SELECT e.first_name, e.last_name, j.job_title
FROM EMPLOYEES as e
INNER JOIN JOB as j
ON j.job_id = e.job_id

-- Show employee name, salary, and pay grade.
SELECT e.first_name, e.last_name, s.salary, s.pay_grade
FROM EMPLOYEES as e
INNER JOIN SALARIES as s
ON e.employee_id = s.employee_id

-- List employees working in the IT department.
SELECT e.first_name,e.last_name,d.dept_name
FROM EMPLOYEES as e
INNER JOIN DEPARTMENT as d
ON e.department_id = d.dept_no
WHERE dept_name = 'Information Technology'

-- Show employees with Senior job level.
SELECT e.first_name, e.last_name, j.job_level
FROM EMPLOYEES as e
INNER JOIN JOB as j
ON j.job_id = e.job_id
WHERE j.job_level = 'senior'