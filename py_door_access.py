import sqlite3

conn = sqlite3.connect('/home/pi/door_access/door_access/door_access.db')
c = conn.cursor()

c.execute('select * from Control')
for row in c:
    (ControlID, CardID, DoorID) = row
    print(row)
    print('ControlID;', ControlID)
    print('CardID;', CardID)
    print('DoorID;', DoorID)
    
