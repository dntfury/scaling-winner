import socket
import sys
import os
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
<head><title>TCP server</title></head>
<body>
<h1>Hello!!, World! from TCP server</h1>
<img src="https://raw.githubusercontent.com/dntfury/scaling-winner/master/server_client_part_1/Screenshot%20(61).png" alt="img" width="200" height="200">
</body>
</html>"""
        http_response= http_response + b"""hello"""
        
        client_connection.sendall(http_response)
        client_connection.close()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

