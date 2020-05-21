from machine import Pin, I2C, RTC, Timer
import machine
import time
#https://github.com/robert-hh/BME280
import bme280_float as bme280
import ujson as json
import usocket as socket
import network

#Network config
ESSID = 'temp_display'
PASSW = '88888888'
DISP_IP = '192.168.0.4'
PORT = 8080

SENSOR_NAME = 'Sensor1'

#Put device to sleep for 5 seconds
def dsleep():
    #Configure RTC.ALARM0 to be able to wake the device
    rtc = RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    #Set RTC.ALARM0 to fire after 5 seconds (waking the device)
    rtc.alarm(rtc.ALARM0, 5000)

    #Go to sleep
    machine.deepsleep()

#Connect to display
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to display...')
    sta_if.active(True)
    sta_if.connect(ESSID, PASSW)

    #Use timer to reset if connection fails
    tim = Timer(-1)
    tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t: dsleep())
    while not sta_if.isconnected():
        pass
    tim.deinit()

print('network config:', sta_if.ifconfig())

#Read data from the sensor
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

data = bme.values
json_data = json.dumps({"sensor_name": SENSOR_NAME, "temperature": data[0], "pressure": data[1], "humidity": data[2]})

#Send data to display
addr = socket.getaddrinfo(DISP_IP, PORT)[0][-1]
s = socket.socket()
s.connect(addr)
sent = s.write(json_data)
s.close()
print('Bytes sent:', sent)

#Data sending somehow fails without this
time.sleep(1)

#Go to sleep
dsleep()