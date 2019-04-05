def read(self):

    d = None
    #if self.config['dht_type'] == 11:
    #  d = dht.DHT22(machine.Pin(self.config["gpio"]))
    #else:
    d = dht.DHT11(machine.Pin(34))
      
    try:
      d.measure()
      payload = { 'temperature': str(d.temperature()), "humidity": str(d.humidity()) }
      return payload
      print(payload)
    except Exception as e:
      Util.log(self,"DHT type: {}, failed to measure pin: '{}'".format(self.config["dht_type"], self.config["gpio"]))
      import sys
      sys.print_exception(e) 