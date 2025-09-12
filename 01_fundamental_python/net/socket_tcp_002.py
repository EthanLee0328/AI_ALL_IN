"""tcp客户端"""

import socket

# 创建tcp套接字
tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# 连接服务器
server_ip = "127.0.0.1"
server_port = 8080
tcp_socket.connect((server_ip, server_port))
while True:
  try:
 # 发送数据
      tcp_socket.send(input(f"{server_ip}:{server_port}<< ").encode("utf-8"))
 # 接收数据
      recv_data = tcp_socket.recv(1024)
      print(f"{server_ip}:{server_port}>> {recv_data.decode("utf-8")}")
  except KeyboardInterrupt:

    break
# 关闭套接字
tcp_socket.close()