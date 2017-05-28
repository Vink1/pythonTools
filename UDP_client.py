import socket
#set port and host
target_host = "127.0.0.1"
target_port = 80    

#use the udp portocol
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#send some data
client.sendto("AAAAAAAAABBBBB",(target_host,target_port))

#recv some data
data, addr = client.recvfrom(4096)

print data