import http.client
import json

PORT = 8000
SERVER= 'localhost'


print('\nConnecting to server: {}:{}\n.'.format(SERVER,PORT))

#connect with the server
conn= http.client.HTTPConnection(SERVER,PORT)


#listspecies
conn.request("GET", '/listSpecies?&json=1')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)




#karyotype
conn.request("GET", '/karyotype?specie=mouse&json=1')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)



#chromosomelenght
conn.request("GET", '/chromosomeLength?specie=mouse&chromo=18&json=1')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)

#genesequence
conn.request("GET", '/geneSeq?gene=FRAT1&json=1   ')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)

#geninfo
conn.request("GET", '  /geneInfo?gene=FRAT1&json=1  ')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)


#genecal
conn.request("GET", '/geneCal?gene=FRAT1&json=1')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)

#genelist
conn.request("GET", '/geneList?chromo=1&start=0&end=30000&json=1')
r1=conn.getresponse()
print('response recieved!: {}{}\n'.format(r1.status,r1.reason))
data1=r1.read().decode('utf-8')
response= json.loads(data1)

print(response)





