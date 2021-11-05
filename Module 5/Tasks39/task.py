import sqlite3

conn = sqlite3.connect('HW.db')

cur = conn.cursor()


cur.execute("""SELECT first_name, last_name, round(salary/12, 2) as 'Monthly Salary' FROM employees""")
rows = cur.fetchall()

[print(row) for row in rows]


conn.close()
