

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
    port = 100
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
        print("Connect to WLAN")
        url = "https://shielded-tor-11299.herokuapp.com/postdata"
        headers = {'content-type': 'application/json'}
        data = {'message': 'WLAN connected'}
        jsonObj = json.dumps(data)
        resp = urequests.post(url, data=jsonObj, headers=headers)
        sleep_ms(1000)  # hold on for 1 second
        print("Request was sent!")

    def main():
        connectWifi(SSID, PASSWORD)
        try:
            url = "https://shielded-tor-11299.herokuapp.com/postdata"
            headers = {'content-type': 'application/json'}
            data = {"message": "jes"}
            jsonObj = json.dumps(data)
            resp = urequests.post(url, data=jsonObj, headers=headers)
        except Exception as e:
            print(e)

    main()

except Exception as e:
    print(e)
