import network
import usocket as socket
import ujson as json

ESSID = 'temp_display'
PASSW = '88888888'

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid=ESSID, password=PASSW, hidden=True)
ap_if.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '1.1.1.1'))

addr = socket.getaddrinfo('0.0.0.0', 8080)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on:', addr)

cl, addr = s.accept()
print('client connected from:', addr)
receive = cl.read()
data = json.loads(receive)
print('Received data:', data)