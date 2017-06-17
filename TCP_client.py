#-*-coding:utf-8-*-
import socket
#set the TCPServer and port
target_host = "127.0.0.1"
target_port = 9999
#use the ipv4 protocol and TCP protocol
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect to the target_host
client.connect((target_host,target_port))
#send some data
client.send("abd")
#put buffer(size is 4096kb) to the1 response
response = client.recv(4096)

def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    try:
        #connect to host
        client.connect((target,host))
        
        if len(buffer):
            client.send(buffer)
        while True:
            #waiting the data recv
            recv_len = 1
            response = ""
            
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                
                if recv_len < 4096:
                    break
            print response
            
            #waiting more input 
            buffer = raw_input("")
            buffer += "\n"
            
            #send those data
            client.send(suffer)
    except:
        print "[*] Exception! Exting."
        #close connect
        client.close()