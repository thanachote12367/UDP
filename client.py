import socket

address = ("127.0.0.1",4999)
number = raw_input("enter your number: ")
number = str(number)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print "send "+number
    s.sendto(number, address)

    data, addr = s.recvfrom(1024)
    print "received data: "+data
    break
s.close()
