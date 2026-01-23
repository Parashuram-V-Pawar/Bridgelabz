CREATE DATABASE employee

use employee;

CREATE TABLE DEPARTMENT (
	dept_no INTEGER PRIMARY KEY,
	dept_name VARCHAR(30) NOT NULL,
	dept_location VARCHAR(50)
);

CREATE TABLE JOB (
	job_id INTEGER PRIMARY KEY,
	job_title VARCHAR(50) NOT NULL,
	job_level VARCHAR(30)
);

CREATE TABLE EMPLOYEES(
	employee_id INTEGER PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	gender VARCHAR(10),
	hire_date DATE,
	department_id INTEGER,
	job_id INTEGER,
	 CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES DEPARTMENT(dept_no),
    CONSTRAINT fk_job
        FOREIGN KEY (job_id)
        REFERENCES JOB(job_id)
);

CREATE TABLE SALARIES(
	salary_id INTEGER PRIMARY KEY,
	employee_id INTEGER NOT NULL,
	salary DECIMAL(10,2),
	bonus DECIMAL(10,2),
	pay_grade CHAR(1),
	CONSTRAINT fk_employee
		FOREIGN KEY(employee_id)
		REFERENCES EMPLOYEES(employee_id)
);