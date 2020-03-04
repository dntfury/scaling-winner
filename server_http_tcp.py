import socket
import sys
import os
import io
HOST, PORT = 'localhost', 8080

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Listening on port {PORT} ...')
while True:
    try:
        client_connection, client_address = listen_socket.accept()
        request_data = client_connection.recv(1024)
        print(request_data.decode('utf-8'))
#the html responce start from the start of line and require the one line break to load in chrome browser
        http_response = b"""\HTTP/1.1 200 OK 

<html>
<body>
<h1>Hello!!, World!</h1>
<img src="http://www.sample_image_link.jpeg">
</html>
</body>"""
        http_response= http_response + b"""hello"""
        
        client_connection.sendall(http_response)
        client_connection.close()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


#fp = open(r"C:\Users\dntfury\Documents\Python Scripts\abc.gif")
#f=io.TextIOWrapper(io.BytesIO(fp), 'utf-8')
#http_response= http_response + f
