#-*-coding:utf-8-*-
import threading
import paramiko
import subprocess
#only execute one command
def ssh_command(ip,user,passwd,command):
    client = paramiko.SSHClient()
    #client.load_host_key('key's path)
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024)
    return 
ssh_command("192.168.186.130", "root", "081455", "id")