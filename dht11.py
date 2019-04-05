try:
    from time import sleep_ms, ticks_ms
    from machine import I2C, Pin, DAC, PWM
    import dht
    import network
    import urequests
    import machine
    import json
    import gc
    import micropython

    SSID = "Xperia X"
    PASSWORD = "lumia1020"
    port = 500
    wlan = None
    s = None

    d = dht.DHT11(Pin(34))

    #sensor pins are set here
    #pot = ADC(Pin(34))
    #pot.width(ADC.WIDTH_10BIT)
    #pot.atten(ADC.ATTN_6DB)

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

        counter = 0
        values1 = []
        values2 = []
        connectWifi(SSID, PASSWORD)
        secondsCounter = 0
        
        while True:
            counter += 1
            temperature = d.temperature()  # get the temperature
            print(temperature)
            message1 = "Temperature: " + str(int(temperature))
            if(len(values1) <= 30):  # start filling the values list
                values1.insert(0, int(temperature))
            else:  # if the list has 30 values, start cycling the list
                values1.remove(values1[29])
                values1.insert(0, int(temperature))

            humidity = d.humidity()  # get the humidity
            print(humidity)
            message2 = "Humidity: " + str(int(humidity))
            if(len(values2) <= 30):  # start filling the values list
                values2.insert(0, int(humidity))
            else:  # if the list has 30 values, start cycling the list
                values2.remove(values2[29])
                values2.insert(0, int(humidity))

            sleep_ms(2000)

            if(counter == 30):  # if 30 values have been added, count the average temperature
                avg1 = sum(values1) / len(values1)
                avg2 = sum(values2) / len(values2)
                counter = 0
            sleep_ms(1000)  # wait one seconds before measuring again
            secondsCounter += 1
            print("Seconds count: " + str(secondsCounter) + " " + message1 + " " + message2)

            if (secondsCounter % 30 == 0):
                gc.collect()  # Collect memory garbage
                # micropython.mem_info()
                # print('Initial free: {} allocated: {}'.format(
                #     gc.mem_free(), gc.mem_alloc()))
                try:
                    data = {"value": avg1 + avg2}
                    jsonObj = json.dumps(data)
                    resp = urequests.post(url, data=jsonObj, headers=headers)
                    print("Request was sent! Value: " + str(avg1 + avg2))
                    resp.close()  # close the response socket to free memory
                    secondsCounter = 0

                except Exception as e:
                    connectWifi(SSID, PASSWORD)
                    print(e)

    main()

except Exception as e:
   print("Error 2")