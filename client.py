import socket
import termcolor
from Seq import Seq

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8082

while True:

    enviar= ("") #lo que voy a mandar hacia el otro lado, paquete grandde
    msg=str(input('>')) #comando, cadena de adn, len compliment etc
    while len(msg)> 0: #mientras la longitud sea mayor que 0

        enviar= enviar + msg + '\n' #lo que envio en su totalidad mas el nuevo mensaje, cada comando lleva un salto de linea
        msg=str(input(' ')) #vas concatenando hasta que la longitud sea 0 y enton es sale del bucle

    if (len(enviar)== 0): #si la longitud detodo el parquete es 0 , envias un paquete vacio para que sepas que estas ahi, estas testeando que el servidor esta al otro ladp

        enviar= enviar + '\n'







    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))


    # Send the request message to the server
    s.send(str.encode(enviar))

    # Receive the servers respoinse
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

    s.close()