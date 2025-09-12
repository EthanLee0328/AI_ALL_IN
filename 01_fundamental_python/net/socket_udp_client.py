import socket

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_ip = "127.0.0.1"
server_port = 8089

while True:
    try:
        msg = input(f"{server_ip}:{server_port}<<")  # 先获取输入
        udp_socket.sendto(msg.encode("utf-8"),(server_ip, server_port))
        recv_data, addr = udp_socket.recvfrom(1024)
        client_ip, client_port = addr
        print(f"{client_ip}:{client_port}>>{recv_data.decode("utf-8")}")

    except KeyboardInterrupt:

        break

udp_socket.close()
