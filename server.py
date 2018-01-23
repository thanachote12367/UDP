import socket

def factorial(n):
    # print(n)
    if int(n) == 0:
        return 1
    else:
        c = int(n) * factorial(int(n)-1)
        # print type(c)
        return c

address = ("127.0.0.1", 4999)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
print "active...."
while True:
    data, addr = s.recvfrom(1024)
    if not data: break
    print "address:{}".format(addr)
    num = factorial(data)
    s.sendto(str(num), addr)
    print "sent to "+str(num)
    break
s.close()