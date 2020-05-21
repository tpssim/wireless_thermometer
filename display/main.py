import network
import usocket as socket
import ujson as json

#Network config
ESSID = 'temp_display'
PASSW = '88888888'
IP = '192.168.0.4'
MASK = '255.255.255.0'
GATEWAY = '192.168.0.1'
DNS = '1.1.1.1'
PORT = 8080

#Variables
sens_name = 'Sensor 1'
sens_temp = '0.0'
sens_pa = '0.0'
sens_hum = '0.0'

oled_width = 128
oled_heigth = 64

def refreshdisp():
    #Title
    oled.text(sens_name, 0, 4)

    #Sensor values
    oled.text('Temp. ' + sens_temp, 0, 20)
    oled.text('PA    ' + sens_pa, 0, 36)
    oled.text('Hum.  ' + sens_hum, 0, 52)

    #Refresh display
    oled.show()

#Init the display
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled = ssd1306.SSD1306_I2C(oled_width, oled_heigth, i2c)
refreshdisp()

#Configure network
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid=ESSID, password=PASSW, hidden=True)
ap_if.ifconfig((IP, MASK, GATEWAY, DNS))

#Setup socket
addr = socket.getaddrinfo('0.0.0.0', PORT)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on:', addr)

#Accept connections to socket
while(1):
    cl, addr = s.accept()
    print('client connected from:', addr)
    receive = cl.read()
    data = json.loads(receive)
    cl.close()
    print('Received data:', data)
    sens_name = data['sensor_name']
    sens_temp = data['temperature']
    sens_pa = data['pressure']
    sens_hum = data['humidity']
    refreshdisp()
