

try:
    from time import sleep_ms, ticks_ms
    from machine import I2C, Pin, DAC, PWM
    from hcsr04 import HCSR04
    import network
    import urequests
    import machine
    import json
    import gc
    import micropython

    SSID = "ZyXEL_2109"#"hh3dlabs"
    PASSWORD = "PKQK8JJKJ7NJL"#"3dlabshh12345"
    port = 200
    wlan = None
    s = None

    # sensor pins are set here
    sensor = HCSR04(trigger_pin=17, echo_pin=4)

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

    def main():

        url = "https://shielded-tor-11299.herokuapp.com/postdata"
        headers = {'content-type': 'application/json'}

        values = []
        counter = 0  # sensor value counter

        connectWifi(SSID, PASSWORD)
        secondsCounter = 0
        while True:
            counter += 1
            distance = sensor.distance_cm()  # get the distance
            message = "Distance: " + str(int(distance)) + " cm"
            if(len(values) <= 30):  # start filling the values list
                values.insert(0, int(distance))
            else:  # if the list has 30 values, start cycling the list
                values.remove(values[29])
                values.insert(0, int(distance))

            if(counter == 30):  # if 30 values have been added, count the average distance
                avg = sum(values) / len(values)
                counter = 0
            sleep_ms(1000)  # wait one seconds before measuring again
            secondsCounter += 1
            print("Seconds count: " + str(secondsCounter) + " " + message)

            if (secondsCounter % 30 == 0):
                gc.collect()  # Collect memory garbage
                # micropython.mem_info()
                # print('Initial free: {} allocated: {}'.format(
                #     gc.mem_free(), gc.mem_alloc()))
                try:
                    data = {"value": avg}
                    jsonObj = json.dumps(data)
                    resp = urequests.post(url, data=jsonObj, headers=headers)
                    print("Request was sent! Value: " + str(avg))
                    resp.close()  # close the response socket to free memory
                    secondsCounter = 0

                except Exception as e:
                    connectWifi(SSID, PASSWORD)
                    print(e)

    main()

except Exception as e:
    print("Error 2")
