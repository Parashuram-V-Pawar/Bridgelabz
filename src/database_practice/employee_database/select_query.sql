/* SELECT Query Demonstration.*/

-- Displaying data of all tables
SELECT * FROM DEPARTMENT;
SELECT * FROM JOB;
SELECT * FROM EMPLOYEES;
SELECT * FROM SALARIES;

-- Displaying first name, last name and gender of all employees
SELECT first_name, last_name, gender from EMPLOYEES;

-- Displaying all departments from department table
SELECT dept_name from DEPARTMENT;

-- Displaying job title and job level from job table
SELECT job_title, job_level from JOB;

-- Displaying all salaries
SELECT salary from SALARIES;