import socket
import time

UDP_IP = "192.168.1.5"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Heartbeat server started ...")

count = 1

while True:
    data, addr = sock.recvfrom(1024)

    time_str = time.ctime(float(data))

    log_str = str(count) + ": " + time_str + \
    ", addr: " + addr[0]  + ":" + str(addr[1])

print(log_str)

count += 1  