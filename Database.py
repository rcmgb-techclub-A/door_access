
import sqlite3
conn = sqlite3.connect("C:\Users\codeclub\door_access\door_access.db")
c = conn.cursor()
def read_from_db():
  c.execute("SELECT * FROM People")
  data = c.fetchall()
  print data
read_from_db()
c.close()

