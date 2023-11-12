import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))


server.listen(5) # maximum backlog of 5 connections

print("[*] Listening on %s:%d" % (bind_ip, bind_port))

# client-handling threa
def handle_client(client_socket):

    # print what the client sends
    request = client_socket.recv(1024)
    request_utf8 = request.decode('utf-8')
    print(f"[*] Received: {request_utf8}")

    # send a packet
    response_str = "Here is your response".encode('utf-8', errors='ignore')
    client_socket.send(response_str)

    client_socket.close()

while True:

    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    # client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()