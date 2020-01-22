from machine import Pin, I2C
from time import sleep
import ssd1306

#amount of connected sensors(1 or 2)
SENSORS = 1

sens1_name = 'Sensor 1'
sens1_temp = 0.0
sens1_pa = 0.0
sens1_hum = 0.0

sens2_name = 'Sensor 2'
sens2_temp = 0.0
sens2_pa = 0.0
sens2_hum = 0.0

oled_width = 128
oled_heigth = 64

#Init the display
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(oled_width, oled_heigth, i2c)

if(SENSORS == 1):
    #Title
    oled.text(sens1_name, 0, 4)

    #Sensor values
    #With only one sensor there is plenty of room on the screen
    oled.text('Temp. ' + str(sens1_temp) + 'C', 0, 20)
    oled.text('PA    ' + str(sens1_pa) + 'hPa', 0, 36)
    oled.text('Hum.  ' + str(sens1_hum) + '%', 0, 52)

elif(SENSORS == 2):
    #Split the screen
    oled.vline(64, 0, 64, 1)
    #Titles
    oled.text(sens1_name, 0, 4)
    oled.text(sens2_name, 65, 4)

    #Sensor 1 values
    #Max length of any value is 5 caracters
    if(sens1_temp < 0):
        oled.text('T.' + str(sens1_temp), 0, 20)
    else:
        oled.text('T. ' + str(sens1_temp), 0, 20)
    if(sens1_pa >= 1000):
        oled.text('PA ' + str(round(sens1_pa)), 0, 36)
    else:
        oled.text('PA ' + str(round(sens1_pa, 1)), 0, 36)   
    #Humidity can't be more than 5 caracters long
    oled.text('H. ' + str(sens1_hum), 0, 52)

    #Sensor 2 values
    #Max length of any value is 5 caracters
    if(sens2_temp < 0):
        oled.text('T.' + str(sens2_temp), 65, 20)
    else:
        oled.text('T. ' + str(sens2_temp), 65, 20)
    if(sens2_pa >= 1000):
        oled.text('PA ' + str(round(sens2_pa)), 65, 36)
    else:
        oled.text('PA ' + str(round(sens2_pa, 1)), 65, 36)   
    #Humidity can't be more than 5 caracters long
    oled.text('H. ' + str(sens2_hum), 65, 52)


oled.show()