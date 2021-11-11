-- 1
SELECT first_name, last_name, department_id, depart_name FROM employees
JOIN departments USING(department_id) ORDER BY department_id DESC;
-- 2
SELECT first_name, last_name, depart_name, city, state_province FROM employees, locations
JOIN departments USING(location_id) ORDER BY location_id DESC;
-- 3
SELECT first_name, last_name, department_id, depart_name FROM employees
JOIN departments USING(department_id) WHERE department_id == 60 OR department_id == 80;
-- 4
SELECT DISTINCT depart_name, department_id FROM departments
LEFT JOIN employees USING(department_id);
-- 5
SELECT E.first_name AS "Employee Name",
       M.first_name AS "Manager"
FROM employees E
JOIN employees M ON E.manager_id = M.employee_id;
-- 6
SELECT jobs.job_title AS "Job Title", employees.first_name || " " || employees.last_name AS "Full Name",
       (jobs.max_salary - employees.salary) as "MAXIMUM Salary Difference"
FROM employees
JOIN jobs USING(job_id);
-- 7
SELECT DISTINCT job_title, ((jobs.max_salary+jobs.min_salary)/2) AS "Average salary" FROM employees
JOIN jobs USING(job_id);
-- 8
SELECT employees.first_name || " " || employees.last_name AS 'full name', employees.salary FROM employees
JOIN departments USING(department_id) WHERE (SELECT department_id FROM departments
JOIN locations USING (location_id) WHERE city == 'London');
-- 9
SELECT COUNT(employees.department_id) AS 'Amount in Department', depart_name
FROM employees, departments
WHERE employees.department_id = departments.department_id
GROUP BY employees.department_id;