import socket


udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind(("127.0.0.1", 8089))

while True:
    recv_data, client_addr = udp_socket.recvfrom(1024)
    client_ip = client_addr[0]
    client_port = client_addr[1]
    print(f"{client_ip}:{client_port}>>{recv_data.decode("utf-8")}")

    udp_socket.sendto("hello".encode("utf-8"), client_addr)

udp_socket.close()
