#!/user/bin/python
import RPi.GPIO as GPIO
import machine 
import network
import json
import micropython
from machine import I2C, Pin, DAC, PWM

#Sensor Pins
sensor = HCSR04(trigger_pin=16, echo_pin=2)


def callback(sensor):
    print "1"
    
GPIO.add_event_detect(sensor, GPIO.BOTH,
bouncetime=300) # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(sensor, callback) # assign function to GPIO PIN, Run function on change

#infinite loop
while True:
    time.sleep(1)