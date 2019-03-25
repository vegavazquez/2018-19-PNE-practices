import http.client
import json
import termcolor
from Seq import Seq


PORT= 80
SERVER= 'rest.ensembl.org'

conn= http.client.HTTPConnection(SERVER, PORT)
conn.request('GET', '/homology/symbol/human/FRAT1?content-type=application/json')
r1= conn.getresponse()
data1=r1.read().decode("utf-8")
respuesta=json.loads(data1)
id= respuesta['data'][0]['id']
print(id)



conn.request('GET', "/sequence/id/"+ id +'?content-type=application/json')
r1= conn.getresponse()
data1=r1.read().decode("utf-8")
respuesta= json.loads(data1)
print(respuesta)
cadena=respuesta['seq']
print(cadena)


S1=Seq(cadena)

print("the lenght of the sequence is : ", len(cadena))


print('T', S1.count('T'))



if S1.perc('A') > S1.perc('T') > S1.perc('G') > S1.perc('C') :
    print("A is the most popular one: ",S1.perc('A'))
elif S1.perc('T') > S1.perc('A') > S1.perc('G') > S1.perc('C'):
    print( " T is the most popular one: ", S1.perc('T'))
elif S1.perc('G') > S1.perc('A') > S1.perc('T') > S1.perc('C'):
    print(" G is the most popular one:", S1.perc('G'))
else:
    print("C is the most popular one ",S1.perc('C') )


print('PERC A:', S1.perc('A'))
print('PERC T:', S1.perc('T'))
print('PERC G:', S1.perc('G'))
print('PERC C:', S1.perc('C'))



