import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8089
BUFFER_SIZE = 1024

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((SERVER_IP, SERVER_PORT))
print(f"[Server] Listening on {SERVER_IP}:{SERVER_PORT}")

clients = set()  # 用来记录客户端地址

def receive():
    while True:
        try:
            data, addr = udp_socket.recvfrom(BUFFER_SIZE)
            clients.add(addr)
            print(f"[Client {addr[0]}:{addr[1]}] >> {data.decode('utf-8')}")
        except Exception as e:
            print("Receive error:", e)
            break

# 启动接收线程
threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        msg = input("[Server] << ")
        if msg.strip() == "":
            continue
        # 给所有已知客户端发送消息
        for client_addr in clients:
            udp_socket.sendto(msg.encode("utf-8"), client_addr)
except KeyboardInterrupt:
    print("Server exiting...")
    udp_socket.close()
