
import socket


#help commands for Linix User 
'''
command for check process at post 8081
>lsof -i:8081/tcp

command to kill process at a port 8081
>fuser -k 8081/tcp


'''


#helpful tool Packet Sender

ip ='127.0.0.1'
port = 8081
capacity = 1
#server or listner
def reciver(ip,port,capacity):
    recv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        recv_socket.bind((ip,port))
    except:
        print("Can't create socket at the ip port combo")
        return -1
    
    recv_socket.listen(capacity)
    print("#Listening @=>" + str(ip) + ":" + str(port) )
    
    read_list = [recv_socket]
    while True:
        recv_conn , address =recv_socket.accept()
        print('[+] connection from>>',address)
        data = recv_conn.recv(1024)
        #The decoding type depends on the type of data you are expecting 
        #you can alway use print(data) also , in that case it will print in bytes
        # format probably
        print(data.decode('ascii'))
        recv_conn.close()    

    #tried safe
    recv_socket.close()
    print("port closed Success!")
    return 0

reciver(ip,port,capacity)


