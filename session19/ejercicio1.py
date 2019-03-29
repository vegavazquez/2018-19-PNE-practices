# Example of accessing to the RandomCAT service for getting an URL
# of a random image of a CAT. This clients just print it on
# the console

import http.client
import json

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes/random"
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME) #conectarse al servidor de los gatos


# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse() #guardar la respuesta

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing


# -- Generate the object from the json file
joke=json.loads(text_json) #diccionario
joke=joke["value"]["joke"]
print(joke)








#counting jokes

ENDPOINT = "/jokes/count"
conn = http.client.HTTPSConnection(HOSTNAME) #conectarse al servidor de los gatos


# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse() #guardar la respuesta

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
print(text_json)

# -- Generate the object from the json file
count=json.loads(text_json) #diccionario
count=count["value"]
print(count)



ENDPOINT = "/categories"
conn = http.client.HTTPSConnection(HOSTNAME) #conectarse al servidor de los gatos


# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse() #guardar la respuesta

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
print(text_json)

# -- Generate the object from the json file
categories=json.loads(text_json) #diccionario
categories=categories["value"]

print("number of categories", len(categories))
for i in categories:
    print("categories: ")
    print(i)




