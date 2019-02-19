import socket
from Seq import Seq
IP = "127.0.0.1"
PORT=8081

while True:
    secuencia= input("dame una secuencia: ")
    s1= seq(secuencia)
    s2=s1.compliment()



    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM )

    s.connect((IP,PORT))

    s.send(str.encode(s2.get_strbase()))
    msg= s.recv(2048).decode("utf-8")
    print("message from the server")
    print(msg)
    s.close()
