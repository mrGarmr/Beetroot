-- Display first and last names with alias
SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees;

-- Get unique department IDs
SELECT DISTINCT department_id FROM employees;

-- Get all employee details ordered by first name in descending order
SELECT * FROM employees ORDER BY first_name DESC;

-- Get names, salary, and PF (12% of salary)
SELECT first_name, last_name, salary, (salary * 0.12) AS PF FROM employees;

-- Get maximum and minimum salary
SELECT MAX(salary) AS Max_Salary, MIN(salary) AS Min_Salary FROM employees;

-- Get monthly salary rounded to 2 decimal places
SELECT first_name, last_name, ROUND(salary / 12, 2) AS Monthly_Salary FROM employees;
