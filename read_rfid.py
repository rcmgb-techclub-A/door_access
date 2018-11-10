#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522
import time

reader = SimpleMFRC522.SimpleMFRC522()

GPIO.setup(6, GPIO.OUT)

while True:
	print("Scanning...")
	time.sleep(2)
	try:
       		id, text = reader.read()
       		print("CardID",id)
       		print("CardText",text)
		GPIO.output(6,1)
		time.sleep(1)
		GPIO.output(6,0)		
	except:
		print("Card Scan Failed")

GPIO.cleanup()
