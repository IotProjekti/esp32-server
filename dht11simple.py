import dht
import machine
from time import sleep

d = dht.DHT11(machine.Pin(14))

while True:
    mittaus = d.measure()
    print(mittaus)
    lampo = d.temperature()
    print(lampo)
    kosteus = d.humidity()
    print(kosteus)
    sleep(2)