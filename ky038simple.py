from machine import Pin, ADC
from time import sleep

#Configure ADC for ESP32
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_6DB)

while True:

  pot_value = pot.read()
  print(pot_value)

  sleep(0.1)
