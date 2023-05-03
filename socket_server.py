# socket connect
import socket

# tcp
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as is_socket:
#     is_socket.bind(('127.0.0.1', 50007))
#     is_socket.listen(1)
#     while True:
#         conn, addr = is_socket.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data: {}, addr: {}'.format(data, addr))
#                 conn.sendall(b'Received: ' + data)

# udp
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as is_socket:
    is_socket.bind(('127.0.0.1', 50007))
    while True:
        data, addr = is_socket.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))