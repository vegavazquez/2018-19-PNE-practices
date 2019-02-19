import socket
import termcolor
# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8088


while True:

    msg = input("> ")  #antes del connect, porque si no dejas la linea levantada y bloqueas las conexiones

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))


    # Send the request message to the server
    s.send(str.encode(msg))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()