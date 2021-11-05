import sqlite3

conn = sqlite3.connect('task1')

c = conn.cursor()

conn.execute("""DELETE FROM Workers WHERE id = 2 """)
conn.execute("""UPDATE Workers SET first_name = "Jonathan" WHERE first_name = "John" """)


conn.commit()

conn.close()
