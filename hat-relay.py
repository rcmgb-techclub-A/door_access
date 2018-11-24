import time
import automationhat
import RPi.GPIO as GPIO

while True:
    automationhat.relay.one.off()
    pin = automationhat.input.one.read()
    if pin == 1:
        print("open")
        automationhat.relay.one.on()
        time.sleep(5)
    else:
        print("Closed")
        time.sleep(1)
        

