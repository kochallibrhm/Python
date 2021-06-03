import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# Bc of client and server running on same computer. We can take server like this
SERVER = socket.gethostbyname(socket.gethostname())
# But also it could be kind of like this 
# SERVER = '192.168.1.3' 

ADDR = (SERVER, PORT)

# AF_INET corresponds to IPv4 and SOCK_STREAM corresponds to TCP 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Use SOCK_DGRAM for UDP
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello world!")
input()
send("Hello everyone!")
input()
send("Hello VH!")

send(DISCONNECT_MESSAGE)
