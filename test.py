import sqlite3
conn = sqlite3.connect("C:\Users\codeclub\door_access\door_access.db")
conn.text_factory = str
c = conn.cursor()
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
i = 0
ac= ([r[0] for r in c.fetchall()])
print("Tables")
for col2 in ac:
    i= i+1
    print ("%d.  %s") % (i , str(col2))
table_selected=int(raw_input("What table would you like to use?"))
table_selected=table_selected-1
table= ("SELECT * FROM %s") %(ac[table_selected])
c.execute(table)
bc=c.fetchall()
g = 0
for col2 in bc:
    g= g+1
    #print ("%d.  %s") % (g , str(col2[1]))
    for h in range(1,col2.shape[1]):
        dave = dave.col2[h]
    print(dave)    
        

c.close()
