from machine import Pin, I2C
import ssd1306

#Variables
sens_name = 'Sensor 1'
sens_temp = 0.0
sens_pa = 0.0
sens_hum = 0.0

oled_width = 128
oled_heigth = 64

#Init the display
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(oled_width, oled_heigth, i2c)

#Title
oled.text(sens_name, 0, 4)

#Sensor values
oled.text('Temp. ' + str(sens_temp) + 'C', 0, 20)
oled.text('PA    ' + str(sens_pa) + 'hPa', 0, 36)
oled.text('Hum.  ' + str(sens_hum) + '%', 0, 52)

#Refresh display
oled.show()