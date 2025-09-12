import socket
import threading

# -------------------------
# 配置
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8089
BUFFER_SIZE = 1024
# -------------------------

def run_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind((SERVER_IP, SERVER_PORT))
    print(f"[Server] Listening on {SERVER_IP}:{SERVER_PORT}")

    def receive():
        while True:
            try:
                data, addr = udp_socket.recvfrom(BUFFER_SIZE)
                print(f"[Client {addr[0]}:{addr[1]}] >> {data.decode('utf-8')}")
            except:
                break

    threading.Thread(target=receive, daemon=True).start()

    try:
        while True:
            msg = input("[Server] << ")
            if msg.strip() == "":
                continue
            udp_socket.sendto(msg.encode("utf-8"), ("127.0.0.1", SERVER_PORT))
    except KeyboardInterrupt:
        print("Server exiting...")
        udp_socket.close()

# -------------------------
def run_client():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 随机分配本地端口
    udp_socket.bind(("0.0.0.0", 0))
    print(f"[Client] Local port {udp_socket.getsockname()[1]}")

    def receive():
        while True:
            try:
                data, addr = udp_socket.recvfrom(BUFFER_SIZE)
                print(f"[Server {addr[0]}:{addr[1]}] >> {data.decode('utf-8')}")
            except:
                break

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

# -------------------------
if __name__ == "__main__":
    choice = input("Start as server (s) or client (c)? ")
    if choice.lower() == "s":
        run_server()
    else:
        run_client()
