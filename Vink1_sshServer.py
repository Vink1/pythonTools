#-*-coding:utf-8-*-
import socket
import paramiko
import threading
import sys

#use example key from paramiko

host_key = paramiko.RSAKey(filename="test_rsa.key")
class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'root') and (password == '081455'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
server = sys.argv[1]
ssh_port = int(sys.argv[2])
try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((server,ssh_port))
    sock.listen(100)
    print '[*] Listening for connection.'
    client,addr = sock.accept()
except Exception,e:
    print '[-] Listen failed: ' + str(e)
    sys.exit(1)
print '[+] Got a connection!'

try:
    Vink1Session = paramiko.Transport(client)
    Vink1Session.add_server_key(host_key)
    server = Server()
    try:
        Vink1Session.start_server(server=server)
    except paramiko.SSHException,x:
        print '[-] SSH negotiation failed.'
        
        
    chan = Vink1Session.accept(20)
    print '[+] Authenticated! '
    print chan.recv(1024)
    chan.send('welcome to Vink1_ssh')
    
    
    while True:
        try:
            command = raw_input("Enter Command :").strip("\n")
            if command !='exit':
                chan.send(command)
                print chan.recv(1024) + '\n'
            else:
                chan.send('exit')
                print "exiting"
                Vink1Session.close()
                raise Exception('exit')
        except KeyboardInterrupt:
            Vink1Session.close()
except Exception,e:
    print '[-] Caught exception: ' + str(e)
    try:
        Vink1Session.close()
    except:
        pass
    sys.exit(1)