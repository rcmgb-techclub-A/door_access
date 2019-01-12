
import sqlite3
conn = sqlite3.connect("C:\Users\codeclub\door_access\door_access.db")
c = conn.cursor()
c.execute("SELECT MAX(PeopleID) FROM(People)")
ac= c.fetchone()
ac= int(ac[0])+1
def Insert_into_people():
    a = str(raw_input("What is the first name?"))
    aa = str(raw_input("What is the second name?"))
    ab = str(raw_input("What is their birthyear?"))
    c.execute("INSERT INTO People (PeopleID, FirstName, LastName, DOB) VALUES (?, ?, ?, ?)",
         (ac, a,aa,ab))     
    conn.commit()
Insert_into_people()

c.close()
