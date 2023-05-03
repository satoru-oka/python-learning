# socket connect
import socket

# tcp
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as is_socket:
#     is_socket.connect(('127.0.0.1', 50007))
#     is_socket.sendall(b'Hello')
#     data = is_socket.recv(1024)
#     print(repr(data))

# udp
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as is_socket:
    is_socket.sendto(b'Hello UDP', ('127.0.0.1', 50007))