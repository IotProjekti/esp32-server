

try:
    from time import sleep_ms, ticks_ms
    from machine import I2C, Pin, DAC, PWM
    from hcsr04 import HCSR04
    import network
    import urequests
    import machine
    import json

    SSID = "hh3dlabs"
    PASSWORD = "3dlabshh12345"
    port = 200
    wlan = None
    s = None

    def connectWifi(ssid, passwd):  # function to connect to the Web
        global wlan  # declare a WLAN object
        wlan = network.WLAN(network.STA_IF)  # create a wlan object
        wlan.active(True)  # Activate the network interface
        wlan.disconnect()  # Disconnect the last connected WiFi
        wlan.connect(ssid, passwd)  # connect wifi
        while(wlan.ifconfig()[0] == '0.0.0.0'):  # wait for connection
            sleep_ms(1)
        sleep_ms(1000)  # hold on for 1 second
        print("Connecting to WLAN")
        # url = "https://shielded-tor-11299.herokuapp.com/postdata"
        # headers = {'content-type': 'application/json'}
        # data = {'message': 'WLAN connected'}
        # jsonObj = json.dumps(data)
        # resp = urequests.post(url, data=jsonObj, headers=headers)
        sleep_ms(1000)  # hold on for 1 second
        # print("Request was sent!")

    def main():
        connectWifi(SSID, PASSWORD)
        minuteCounter = 0
        print("In main")
        while True:
            sleep_ms(1000)
            minuteCounter += 1
            if (minuteCounter % 60 == 0):
                try:
                    url = "https://shielded-tor-11299.herokuapp.com/postdata"
                    headers = {'content-type': 'application/json'}
                    data = {"value": minuteCounter}
                    jsonObj = json.dumps(data)
                    resp = urequests.post(url, data=jsonObj, headers=headers)
                    print("Request was sent! Value: " + str(minuteCounter))
                    minuteCounter = 0
                except Exception as e:
                    connectWifi(SSID, PASSWORD)
                    print(e)

    main()

except Exception as e:
    print(e)
