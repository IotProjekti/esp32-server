#!/user/bin/python
import RPi.GPIO as GPIO
import machine 
import network
import json
import micropython
from machine import I2C, Pin, DAC, PWM

def __init__(self, trigger_pin, echo_pin):
        """
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
        echo_timeout_us: Timeout in microseconds to listen to echo pin. 
        By default is based in sensor limit range (4m)
        """
        #self.echo_timeout_us = echo_timeout_us
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.IN, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

#Sensor Pins
sensor = (trigger_pin=16, echo_pin=2)

def callback(sensor):
    print "one"

    else:

         print "two"

GPIO.add_event_detect(sensor, GPIO.BOTH,
bouncetime=300) # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(sensor, callback) # assign function to GPIO PIN, Run function on change

#infinite loop
while True:
    time.sleep(1)