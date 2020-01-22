from machine import Pin, I2C
#https://github.com/robert-hh/BME280
import bme280_float as bme280
import ujson as json
import usocket as socket
import network

ESSID = 'temp_display'
PASSW = '88888888'
SENSOR_NAME = 'Sensor1'

#Connect to display
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to display...')
    sta_if.active(True)
    sta_if.connect(ESSID, PASSW)
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())

#Read data from the sensor
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

data = bme.values
json_data = json.dumps({"sensor_name": SENSOR_NAME, "temperature": data[0], "pressure": data[1], "humidity": data[2]})

#Send data to display
addr = socket.getaddrinfo('192.168.0.4', 8080)[0][-1]
s = socket.socket()
s.connect(addr)
sent = s.write(json_data)
s.close()
print('Bytes sent:', sent)