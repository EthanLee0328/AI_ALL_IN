import socket

tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
tcp_socket.bind(('127.0.0.1', 8080))
tcp_socket.listen(2)
client_socket, client_addr = tcp_socket.accept()
while True:
    data = client_socket.recv(1024)
    print(f'{client_addr[0]}:{client_addr[1]} >> {data.decode("utf-8")}')
    client_socket.send('你好'.encode('utf-8'))

client_socket.close()
tcp_socket.close()
