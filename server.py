import socket
import termcolor
from Seq import Seq


IP = "127.0.0.1"
PORT = 8082

MAX_OPEN_REQUEST= 5




def validSequence(S):
    valid='ACTG'
    for letter in s:
        if letter not in valid:
            return False
        return True

def tratar(s1, comando):
    print(' haciendo comando', comando)
    if (comando== 'len'):
        return s1.len()
    elif (comando== 'complement'):
        return s1.complement().get_strbase()
    elif(comando== 'reverse'):
        return s1.reverse().get_strbase()
    elif (comando== 'countA'):
        return s1.count('A')
    elif (comando== 'countT'):
        return s1.count('T')
    elif (comando== 'countG'):
        return s1.count('G')
    elif (comando== 'countC'):
        return s1.count('C')
    elif (comando== 'percA'):
        return s1.perc('A')
    elif (comando== 'percT'):
        return s1.perc('T')
    elif (comando== 'percG'):
        return s1.perc('G')
    elif (comando== 'percC'):
        return s1.perc('C')
    else:
        return 'ERROR'




def process_client():

    msg= s.recv(2048).decode("utf-8")


    termcolor.cprint(msg, 'red')


    if (msg== '\n'):
        response='ALIVE'

    else:
        trozos= msg.split('\n')
        print( 'valorando', trozos[0])
        if (validsequence(trozos[0])):
            response= 'OK\n'

            s1=seq(trozos[0])


            for i in range(1, len(trozos)-1):
                print('tratando el comando', i, trozos[i])
                r= tratar(s1, trozos[i])
                response=response + str(r) + '\n'


        else:
            response = 'ERROR'
    print('request message: {}'.format(msg))




    cs.send(str.enconde(msg))
    cs.close()

#main programm

#create INET, streaming socket

seversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind the socket to the IP and PORT

seversocket.bind((IP, PORT))
seversocket.listen(MAX_OPEN_REQUEST)

print('socket ready: {}'.format(seversocket))


while True:

        print("waiting for connections at {}, {}".format(IP,PORT))
        (clientsocket, adress)= seversocket.accept()

        print("attending connections from ciient ".format(adress))


