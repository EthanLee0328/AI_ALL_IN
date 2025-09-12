import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8089
BUFFER_SIZE = 1024

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 自动分配本地端口
udp_socket.bind(("0.0.0.0", 0))
print(f"[Client] Local port {udp_socket.getsockname()[1]}")

def receive():
    while True:
        try:
            data, addr = udp_socket.recvfrom(BUFFER_SIZE)
            print(f"[Server {addr[0]}:{addr[1]}] >> {data.decode('utf-8')}")
        except Exception as e:
            print("Receive error:", e)
            break

# 启动接收线程
threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        msg = input("[Client] << ")
        if msg.strip() == "":
            continue
        udp_socket.sendto(msg.encode("utf-8"), (SERVER_IP, SERVER_PORT))
except KeyboardInterrupt:
    print("Client exiting...")
    udp_socket.close()
