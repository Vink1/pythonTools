import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

#5 threading socket max
server.listen(5)

print "[*] Listening on %s:%d" %(bind_ip,bind_port)

#the handle threding to client
def handle_client(client_socket):
    #print client data
    request = client_socket.recv(1024)
    
    print "[*] Received: %s" %request
    
    #resend a data package 
    client_socket.send("ACK!")
    
    client_socket.close()
    
while True:
    client , addr = server.accept()
    
    print "[*] Accepted connection from %s:%d " % (addr[0],addr[1])
    
    #hang up the client threading and conduct the data
    
    client_handler = threading.Thread(target = handle_client,args=(client,))
    client_handler.start()