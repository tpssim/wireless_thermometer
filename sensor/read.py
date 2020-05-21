from machine import Pin, I2C
#https://github.com/robert-hh/BME280
import bme280_float as bme280

#Read data from the sensor
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)
data = bme.values

#Print the data
print("temperature:"+ data[0])
print("pressure:"+ data[1])
print("humidity:"+ data[2])