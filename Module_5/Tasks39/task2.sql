SELECT first_name, last_name FROM employees;

SELECT DISTINCT department_id FROM employees;

SELECT * FROM employees order by first_name DESC;

-- ALTER TABLE employees ADD PF AS ((salary*12) /100);
SELECT first_name, last_name, salary, PF from employees;

SELECT MAX(salary), MIN(salary) FROM employees;

SELECT first_name, last_name, round(salary/12, 2) as 'Monthly Salary' FROM employees;