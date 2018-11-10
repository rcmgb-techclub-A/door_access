#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import sqlite3

reader = SimpleMFRC522.SimpleMFRC522()

GPIO.setup(6, GPIO.OUT)

while True:
        print("Scanning...")
        time.sleep(2)
        try:
                id, text = reader.read()
                print("CardID",id)
                #print("CardText",text)
                
                conn = sqlite3.connect('/home/pi/door_access/door_access/door_access.db')
                c = conn.cursor()
                t = (id,)
                c.execute('SELECT * FROM Control WHERE CardID = ?',t)

                data=c.fetchall()
                
                if len(data)==0:
                        print('There is no user %s' %id)
                else:
                        print('User %s' %id)
                        GPIO.output(6,1)
                        time.sleep(1)
                        GPIO.output(6,0)

        except:
                print("Card Scan Failed")

GPIO.cleanup()







for row in c:
    (ControlID, CardID, DoorID) = row
    print(row)
    print('ControlID;', ControlID)
    print('CardID;', CardID)
    print('DoorID;', DoorID)
