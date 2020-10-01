# scaling-winner

[![branding](https://img.shields.io/badge/TCP-Socket-brightgreen)](https://github.com/dntfury/)
[![branding](https://img.shields.io/badge/Python-Socket-brightgreen)](https://docs.python.org/3/library/socket.html)
[![branding](https://img.shields.io/badge/*-*-brightgreen)](https://github.com/dntfury/scaling-winner/tree/master)

This is a basic peer-2-peer messaging program written in python , the data transfer is done with the sockets(ip,port pair) and can be run in command promt [CMD].This ahve been run in windows , have not tried in other OS.

## How to Run [test in single PC]

> Create Two copies of Program 
> In first copy set the sending <ip,port> in sender function if want as example ('127.0.0.1',8080) this means send messages  to this   
 
> set the listening <port> edit the ip and port in the reciver function if want as ('127.0.0.1',8081) means listen at this

> Similary do opposite in the other copy

> Run both progrm in cmd* by opening two console 
> python <file1>.py 
> python <file2>.py

> Try to send message by entering message

> * try in cmd beacuse in python IDLE it would not work!!! 


# Requirements 
>> python 3+ 

# Note 
> I have also tested this program on different PC'S or laptop and It works only if those PC's are connected to same network and for this you have to change ip s 192.168.1.1 kind of according to your network   

>> will also see updates 