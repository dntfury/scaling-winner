# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:09:01 2018

@author: deshmukh tanul
"""

import socket
import time
import threading

def reciver():
    #sending message do not need to encode
    reciver_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    reciver_socket.bind(('127.0.0.1',8081)) #recive or listen on this
    reciver_socket.listen(1)  #accept one connection only
    print("listenig on 127.0.0.1:8081>>\r\n")
    recived_conn,sender_addr=reciver_socket.accept()
    print('[+] connection from',sender_addr)
    ack=1
    #ack=bytes(ack,'utf-8') this may not work
    ack=bytes(ack)
    recived_conn.send(ack)
    while recived_conn:
        message_recived=recived_conn.recv(1024)
        #message_recived=bytes(message_recived,'utf-8') this may not work
        message_recived=bytes(message_recived)
        quit_string=bytes("0",'utf-8')
        if message_recived==quit_string:
            print("sender want to terminate\r\n")
            print(message_recived)
            print("\r\n****closing connection****\r\n")
            reciver_socket.close()
            print("\r\n----------connection closed---------------\r\n")
            exit(0)
        elif len(message_recived)>1:
            print("\r\n---------------------message recived------------------\r\n")
            print(message_recived)
            print("\r\n---------------------end of message-------------------\r\n")




def sender():
    sender_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("sleeping for 5 sec")
    time.sleep(5)
    print("awaked")
    sender_socket.connect(('127.0.0.1',8080))   #it says connect to this port send connectio to that it
    print("sending con to >>127.0.0.1:8080...\r\n")
    ack=sender_socket.recv(1024)
    #ack=bytes(ack,'utf-8') #recived bytes need not to be encode utf-8
    ack=bytes(ack)
    print("we get",ack)
    if ack:
        print('\n\r----------------------------connected----------------------')
        while sender_socket:
            message_to_sent=input("MESSAGE>> ")
            message_to_sent=bytes(message_to_sent,'utf-8')
            print("we sent",message_to_sent)
            quit_string=bytes("0",'utf-8')
            if(message_to_sent == quit_string):
                print("\r\n----------closing connection---------------\r\n")
                sender_socket.send(message_to_sent)
                sender_socket.close()    #closs session
                print("\r\n----------connection closed---------------\r\n")
                exit(0)
            else:
                sender_socket.send(message_to_sent) #send command
                print("\r\n message sent\r\n")
 


def main():
    reciver_thread=threading.Thread(target=reciver,name='reciver_thread')
    reciver_thread.start()
    sender_thread=threading.Thread(target=sender,name='sender_thread')
    sender_thread.start()
    reciver_thread.join()
    sender_thread.join()

main()            